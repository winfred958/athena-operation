# encoding: utf-8
import logging
import os

region_name = "us-west-2"

athena_s3_result_tmp_path = "s3://yamibuy-oregon/athena/sql_result"

LOG_DIR_NAME = "log"
LOG_FILE_NAME = "athena-operation.log"
LOG_LEVEL = logging.INFO

jar_file_path = "{}/../lib*.jar".format(os.path.split(os.path.realpath(__file__))[0])
