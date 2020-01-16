# encoding: utf-8

import argparse

from ddl.alter_partition import AthenaAlter
from utils.log_utils import LogUtil

log = LogUtil()


def get_parse_args():
    # 获取参数
    parser = argparse.ArgumentParser(description="google cloud operation")
    parser.add_argument("-ac", "--all-config", help="database", action="store",
                        type=str, default=None, required=False)
    parser.add_argument("-d", "--database", help="database", action="store",
                        type=str, required=True)
    parser.add_argument("-t", "--table", help="table", action="store",
                        type=str, required=True)

    parser.add_argument("-p", "--partitions", help="k1=v1,k2=v2,k3=v3", action="store",
                        type=str, default=None)

    parser.add_argument("-l", "--location", help="location", action="store",
                        type=str, default=None)

    parser.add_argument("-o", "--override", help="override", action="store",
                        type=bool, default=False, required=False)

    args = parser.parse_args()

    return AddPartitionRequest(
        database=args.database,
        table=args.table,
        partitions=args.partitions,
        location=args.location,
        override=args.override
    )


class AddPartitionRequest(object):
    def __init__(self, database, table, partitions, location, override):
        self.database = database
        self.table = table
        self.partitions = partitions
        self.location = location
        self.override = override


def check(
        request  # type: AddPartitionRequest
):
    if request.database is None or request.table is None:
        raise Exception("Invalid request")


if __name__ == '__main__':
    request = get_parse_args()
    athena_alter = AthenaAlter(database=request.database, table=request.table, partition_str=request.partitions,
                               location=request.location)
    check(request)

    athena_alter.drop_partition()
    athena_alter.add_partition()
    athena_alter.refresh_partition()
