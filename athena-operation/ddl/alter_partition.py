# encoding: utf-8
from connector.base_dao import BaseDao


class AthenaAlter(BaseDao):
    """

    """

    def __init__(self, database, table, partition_str, location=None, properties=dict):
        super(AthenaAlter, self).__init__(database=database, table=table)
        self.partition_str = partition_str
        self.location = location
        self.properties = properties

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
