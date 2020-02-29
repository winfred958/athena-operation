# encoding: utf-8
import datetime
import unittest

from ddl.alter_partition import AthenaAlter
from entity.add_partition_request import AddPartitionRequest


class AthenaAlterTest(unittest.TestCase):
    """

    """

    def test_add_partition(self):
        request = AddPartitionRequest(
            database="ods",
            table="xxx",
            partitions="dt='2020-01-20'",
            location="s3://xxx/xx/xxx",
            override=True
        )

        athena_alter = AthenaAlter(request=request)
        athena_alter.add_partition()

    def test_datetime(self):
        now = datetime.datetime.now()
        print(now.strftime("year=%Y,month=%m,day=%d"))
        print(now.strftime("location: s3://xxxx/database/table/dt=%Y-%m-%d"))
