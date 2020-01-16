# encoding: utf-8
import json


class AddPartitionRequest(object):
    def __init__(self, database, table, partitions, location, override, all_config=False):
        self.database = database
        self.table = table
        self.partitions = partitions
        self.location = location
        self.override = override
        self.all_config = all_config

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
