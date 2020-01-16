# encoding: utf-8
import datetime
from abc import abstractmethod

from config import config
from connector.connector import AthenaRequestEntity, AthenaConnector


class BaseDao(object):
    """

    """

    def __init__(self, database, table):
        self.database = database
        self.table = table

    def execute_sql(self, sql):
        request = AthenaRequestEntity(
            sql=sql,
            database=self.database,
            result_path=self.__get_result_path(tag=self.get_operation_tag())
        )
        AthenaConnector().execute_sql(request)

    @staticmethod
    def __get_sub_path_name():
        now = datetime.datetime.now()
        return "{}__{}".format(now.strftime("%Y_%m_%d_%H_%M_%S"), now.timestamp())

    def __get_result_path(self, tag="ddl"):
        result_path = "{basePath}/{database}/{table}/{tag}/{file_name}".format(
            basePath=config.athena_s3_result_tmp_path,
            database=self.database,
            tag=tag,
            table=self.table,
            file_name=self.__get_sub_path_name()
        )
        return result_path

    @abstractmethod
    def get_operation_tag(self):
        pass
