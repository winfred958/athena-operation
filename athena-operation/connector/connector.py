# encoding: utf-8


import boto3

from config import auth_config
from config import config


class Connector(object):
    """

    """

    def __init__(self):
        self.region_name = config.region_name
        self.aws_access_key_id = auth_config.aws_access_key_id
        self.aws_secret_access_key = auth_config.aws_secret_access_key

    def get_athena_connector(self):
        """

        :return: athena
        """

        # def client(self, service_name, region_name=None, api_version=None,
        #            use_ssl=True, verify=None, endpoint_url=None,
        #            aws_access_key_id=None, aws_secret_access_key=None,
        #            aws_session_token=None, config=None):

        conf = {
            "service_name": "athena",
            "region_name": self.region_name,
            "aws_access_key_id": self.aws_access_key_id,
            "aws_secret_access_key": self.aws_secret_access_key
        }

        athena = boto3.client(**conf)
        return athena
