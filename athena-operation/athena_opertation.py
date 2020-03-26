# encoding: utf-8

import argparse
import datetime

from ddl.alter_partition import AthenaAlter
from entity.add_partition_request import AddPartitionRequest
from utils.log_utils import LogUtil

log = LogUtil()


def get_parse_args():
    # 获取参数
    parser = argparse.ArgumentParser(description="athena operation")

    # parser.add_argument("-ac", "--all-config",
    #                     help="load partition info from config file, 未实现",
    #                     action="store",
    #                     type=bool, default=False,
    #                     required=False
    #                     )

    parser.add_argument("-d", "--database", help="database", action="store",
                        type=str, required=False)
    parser.add_argument("-t", "--table", help="table", action="store",
                        type=str, required=False)

    parser.add_argument("-pf", "--partition-format", help="eg. "
                                                          "year='%%Y',month='%%m',day='%%d' "
                                                          "OR "
                                                          "dt='%%Y-%%m-%%d'",
                        action="store",
                        type=str,
                        default=None
                        )

    parser.add_argument("-lf", "--location-format",
                        help="eg. "
                             "location: "
                             "s3://xxxx/database/table/dt=%%Y-%%m-%%d "
                             "OR "
                             "s3://xxxx/database/table/%%Y/%%m/%%d",
                        action="store",
                        type=str,
                        default=None
                        )

    parser.add_argument("-sd", "--start-date", help="eg. 2020-02-28", action="store",
                        type=str, default=None)

    parser.add_argument("-ed", "--end-date", help="eg. 2020-02-29", action="store",
                        type=str, default=None)

    parser.add_argument("-o", "--overwrite", help="overwrite", action="store",
                        type=bool, default=False, required=False)

    # try:
    #     known_args = parser.parse_known_args()
    #     log.info(known_args.__dict__)
    # except Exception:
    #     log.error(parser.parse_known_args())

    args = parser.parse_args()

    start_date_str = args.start_date
    end_date_str = args.end_date

    if start_date_str is None:
        start_date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    if end_date_str is None:
        end_date_str = datetime.datetime.now().strftime("%Y-%m-%d")

    try:
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
    except Exception:
        log.error(" start date format error. use default now()")
        start_date = datetime.datetime.now()
    try:
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
    except Exception:
        log.error(" end date format error. use default now()")
        end_date = datetime.datetime.now()

    return AddPartitionRequest(
        database=args.database,
        table=args.table,
        partition_format=args.partition_format,
        location_format=args.location_format,
        start_date=start_date,
        end_date=end_date,
        overwrite=args.overwrite
    )


def check(
        request  # type: AddPartitionRequest
):
    if request.database is None or request.table is None:
        raise Exception("Invalid request: database table missing")
    if request.start_date > request.end_date:
        raise Exception("Invalid request: start-date > end-date")


if __name__ == '__main__':
    request = get_parse_args()
    log.info("[ request ]: {}".format(request.__str__()))

    check(request)
    athena_alter = AthenaAlter(request=request)
    athena_alter.add_partition()
