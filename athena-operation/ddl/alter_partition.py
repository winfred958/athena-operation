# encoding: utf-8
from connector.base_dao import BaseDao
from entity.add_partition_request import AddPartitionRequest


class AthenaAlter(BaseDao):
    """

    """

    def __init__(self,
                 request,  # type: AddPartitionRequest
                 properties=dict
                 ):
        super(AthenaAlter, self).__init__(database=request.database, table=request.table)
        self.partition_str = request.partitions
        self.location = request.location
        self.properties = properties

    def add_partition(self,
                      add_partition_request  # type: AddPartitionRequest
                      ):
        if add_partition_request.all_config:
            # 读取配置
            pass
        else:
            self.add_partition_override()

    def add_partition_override(self):
        self.drop_partition()
        self.add_partition()

    def add_partition(self):
        """

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

    def drop_partition(self):
        """

        :return:
        """

        sql = "ALTER TABLE {database}.{table} DROP IF EXISTS PARTITION ({partition})".format(
            database=self.database,
            table=self.table,
            partition=self.partition_str,
            location=self.location
        )
        self.execute_sql(sql)

    def refresh_partition(self):
        sql = "MSCK REPAIR TABLE {database}.{table}".format(database=self.database, table=self.table)
        self.execute_sql(sql)

    def get_operation_tag(self):
        return "alert_partition"
