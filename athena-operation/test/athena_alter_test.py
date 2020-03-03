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
            table="test",
            partition_format="dt='%Y-%m-%d'",
            location_format="s3://xxx/xx/%Y/%m/%d",
            start_date=datetime.datetime.strptime("2020-02-28", "%Y-%m-%d"),
            end_date=datetime.datetime.strptime("2020-03-01", "%Y-%m-%d"),
            overwrite=True
        )

        athena_alter = AthenaAlter(request=request)
        athena_alter.add_partition()

    def test_datetime(self):
        now = datetime.datetime.now()
        print(now.strftime("year=%Y,month=%m,day=%d"))
        print(now.strftime("year=%Y,month=%m,day=%d location: s3://xxxx/database/table/dt=%Y-%m-%d"))

        print(datetime.datetime.strptime("2020-03-01", "%Y-%m-%d"))

    def test_datetime_compare(self):
        now = datetime.datetime.now()
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        print(type(now))
        print(type(yesterday))
        if now > yesterday:
            print("xxxxxxxxxxx")
