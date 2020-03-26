# encoding: utf-8
import datetime
import os
from abc import abstractmethod

from config import config
from utils.log_utils import LogUtil

log = LogUtil()


class BaseDao(object):
    """

    """

    def __init__(self, database, table):
        self.database = database
        self.table = table

    def execute_sql(self, sql):
        result_path = self.__get_result_path(tag=self.get_operation_tag())
        log.info("[athena execute sql]: {} ; result_path = {}".format(sql, result_path))
        # request = AthenaRequestEntity(
        #     sql=sql,
        #     database=self.database,
        #     result_path=result_path
        # )
        # AthenaConnector().execute_sql(request)
        os.system("java -jar {} {}".format(config.jar_file_path, sql))

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
