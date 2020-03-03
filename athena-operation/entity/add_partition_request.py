# encoding: utf-8
import datetime
import json


class AddPartitionRequest(object):
    def __init__(self,
                 database,
                 table,
                 partition_format,  # type str
                 location_format,  # type str
                 start_date,  # type datetime
                 end_date,  # type datetime
                 override,  # type boolean
                 all_config=False
                 ):
        self.database = database
        self.table = table
        self.partition_format = partition_format
        self.location_format = location_format
        self.start_date = start_date
        self.end_date = end_date
        self.override = override
        self.all_config = all_config

    def __str__(self):
        return json.dumps(self, default=self.json_default, sort_keys=True, indent=4)

    @staticmethod
    def json_default(value):
        if isinstance(value, datetime.datetime):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return value.__dict__