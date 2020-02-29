# encoding: utf-8
import json


class AddPartitionRequest(object):
    def __init__(self, database, table, partition_format, location_format, start_date, end_date, override, all_config=False):
        self.database = database
        self.table = table
        self.partition_format = partition_format
        self.location_format = location_format
        self.start_date = start_date
        self.end_date = end_date
        self.override = override
        self.all_config = all_config

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
