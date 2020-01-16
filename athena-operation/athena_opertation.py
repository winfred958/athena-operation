# encoding: utf-8

import argparse

from ddl.alter_partition import AthenaAlter


def get_parse_args():
    # 获取参数
    parser = argparse.ArgumentParser(description="google cloud operation")
    parser.add_argument("-db", "--database", help="database", action="store",
                        type=str, default=None)
    parser.add_argument("-t", "--table", help="table", action="store",
                        type=str, default=None)

    parser.add_argument("-ps", "--partitions", help="k1=v1,k2=v2,k3=v3", action="store",
                        type=str, default=None)

    parser.add_argument("-l", "--location", help="location", action="store",
                        type=str, default=None)
    parser.add_argument("-o", "--override", help="override", action="store",
                        type=bool, default=False)

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


if __name__ == '__main__':
    request = get_parse_args()
    AthenaAlter(database=request.database, table=request.table, )
