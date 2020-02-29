# encoding: utf-8
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
        self.partition_str = request.partition_format
        self.location = request.location_format
        self.properties = properties

    def add_partition(self):
        if self.request.override:
            self.__add_partition_override()
        else:
            self.__add_partition()
        self.__refresh_partition()

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
        if self.location is None:
            sql = "ALTER TABLE {database}.{table} ADD IF NOT EXISTS PARTITION ({partition})'".format(
                database=self.database,
                table=self.table,
                partition=self.partition_str
            )
        else:
            sql = "ALTER TABLE {database}.{table} ADD IF NOT EXISTS PARTITION ({partition}) LOCATION '{location}'".format(
                database=self.database,
                table=self.table,
                partition=self.partition_str,
                location=self.location
            )
        self.execute_sql(sql)

    def __drop_partition(self):
        """
        drop partition

        eg.
            ALTER TABLE orders
            DROP PARTITION (dt = '2014-05-14', country = 'IN'), PARTITION (dt = '2014-05-15', country = 'IN');
        :return:
        """
        sql = "ALTER TABLE {database}.{table} DROP IF EXISTS PARTITION ({partition})".format(
            database=self.database,
            table=self.table,
            partition=self.partition_str,
            location=self.location
        )
        self.execute_sql(sql)

    def __refresh_partition(self):
        """
        refresh partition
        :return:
        """
        sql = "MSCK REPAIR TABLE {database}.{table}".format(database=self.database, table=self.table)
        self.execute_sql(sql)

    def get_operation_tag(self):
        return "alert_partition"
