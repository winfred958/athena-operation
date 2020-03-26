# encoding: utf-8
import datetime
import time

from connector.base_dao import BaseDao
from entity.add_partition_request import AddPartitionRequest
from utils.log_utils import LogUtil

log = LogUtil()


class AthenaAlter(BaseDao):
    """
    
    """

    def __init__(self,
                 request,  # type: AddPartitionRequest
                 properties=dict
                 ):
        super(AthenaAlter, self).__init__(database=request.database, table=request.table)
        self.request = request
        self.properties = properties

    def add_partition(self):
        if self.request.overwrite:
            self.__add_partition_override()
        else:
            self.__add_partition()
        # self.__refresh_partition()

    def __add_partition_from_config_file(self):
        """
        FIXME: 暂未实现
        :return:
        """
        pass

    def __add_partition_override(self):
        self.__drop_partition()
        self.__add_partition()

    def __add_partition(self):
        """
        add partition

        eg.
            ALTER TABLE orders ADD
            PARTITION (dt = '2016-05-14', country = 'IN') LOCATION 's3://mystorage/path/to/INDIA_14_May_2016/'
            PARTITION (dt = '2016-05-15', country = 'IN') LOCATION 's3://mystorage/path/to/INDIA_15_May_2016/';
        :return:
        """
        if self.request.location_format is not None:
            partitions = self.__get_partition(segmentation=" ", with_location=True)
        else:
            partitions = self.__get_partition(segmentation=" ")
        sql = "ALTER TABLE {database}.{table} ADD IF NOT EXISTS {partitions}".format(
            database=self.database,
            table=self.table,
            partitions=partitions
        )
        log.debug("[SQL]: {}".format(sql))
        self.execute_sql(sql)

    def __drop_partition(self):
        """
        drop partition

        eg.
            ALTER TABLE orders DROP
            PARTITION (dt = '2014-05-14', country = 'IN'),
            PARTITION (dt = '2014-05-15', country = 'IN');
        :return:
        """
        sql = "ALTER TABLE {database}.{table} DROP IF EXISTS {partitions}".format(
            database=self.database,
            table=self.table,
            partitions=self.__get_partition(segmentation=", ")
        )
        log.debug("[SQL]: {}".format(sql))
        self.execute_sql(sql)

    def __refresh_partition(self):
        """
        refresh partition
        :return:
        """
        sql = "MSCK REPAIR TABLE {database}.{table}".format(
            database=self.database,
            table=self.table
        )
        log.debug("[SQL]: {}".format(sql))
        self.execute_sql(sql)

    def __get_partition(self,
                        segmentation,  # type: str
                        with_location=False
                        ):
        """
        :param :
        :return:
        """
        str_format = "PARTITION ({partition_kv})"
        str_format_with_location = "PARTITION ({partition_kv}) LOCATION '{location}'"

        start_date = self.request.start_date
        end_date = self.request.end_date
        partition_format = str(self.request.partition_format)
        location_format = self.request.location_format
        partition_set = set()

        while start_date <= end_date:
            partition_kv = start_date.strftime(partition_format)
            location = start_date.strftime(location_format)
            sub_str = str_format.format(partition_kv=partition_kv)
            if with_location:
                sub_str = str_format_with_location.format(
                    partition_kv=partition_kv,
                    location=location
                )
            partition_set.add(sub_str)
            start_date = start_date + datetime.timedelta(days=1)
        return segmentation.join(partition_set)

    def get_operation_tag(self):
        return "alert_partition"
