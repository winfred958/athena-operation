# encoding: utf-8


import boto3

from config import auth_config
from config import config


class AthenaConnector(object):
    """

    """

    def __init__(self):
        self.region_name = config.region_name
        self.aws_access_key_id = auth_config.aws_access_key_id
        self.aws_secret_access_key = auth_config.aws_secret_access_key

    def get_athena_connector(self):
        """
        athena connector
        :return: athena
        """
        conf = {
            "service_name": "athena",
            "region_name": self.region_name,
            "aws_access_key_id": self.aws_access_key_id,
            "aws_secret_access_key": self.aws_secret_access_key
        }

        athena = boto3.client(**conf)
        return athena

    def execute_sql(
            self,
            request  # type: AthenaRequestEntity
    ):
        """
        execute sql
        :param request:
        QueryString : sql
        QueryExecutionContext: database
        ResultConfiguration:
        :return:
        """
        self.get_athena_connector().start_query_execution(**request.get_request_object())


class AthenaRequestEntity(object):

    def __init__(self, sql, database, result_path):
        self.sql = sql
        self.database = database
        self.result_path = result_path

    def get_request_object(self):
        query_execution_context = {
            "Database": self.database
        }
        result_configuration = {
            "OutputLocation": self.result_path
        }
        return {
            "QueryString": self.sql,
            "QueryExecutionContext": query_execution_context,
            "ResultConfiguration": result_configuration
        }
