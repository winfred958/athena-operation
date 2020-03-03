# athena-operation

## 1. clone
  > * git clone https://github.com/winfred958/athena-operation.git
## 2. system env config
  > * export AWS_ACCESS_KEY_ID=xxx
  > * export AWS_SECRET_ACCESS_KEY=xxx
## 3. config
  > * vim athena-operation/config/config.py
  > > * region_name
  > > * athena_s3_result_tmp_path
  > > * LOG_LEVEL
## 4. use
### 4.1 show help
  > * sh ./bin/add_partition.sh --help
```text
usage: athena_opertation.py [-h] [-d DATABASE] [-t TABLE]
                            [-pf PARTITION_FORMAT] [-lf LOCATION_FORMAT]
                            [-sd START_DATE] [-ed END_DATE] [-o OVERWRITE]

athena operation

optional arguments:
  -h, --help            show this help message and exit
  -d DATABASE, --database DATABASE
                        database
  -t TABLE, --table TABLE
                        table
  -pf PARTITION_FORMAT, --partition-format PARTITION_FORMAT
                        eg. year='%Y',month='%m',day='%d' OR dt='%Y-%m-%d'
  -lf LOCATION_FORMAT, --location-format LOCATION_FORMAT
                        eg. location: s3://xxxx/database/table/dt=%Y-%m-%d OR
                        s3://xxxx/database/table/%Y/%m/%d
  -sd START_DATE, --start-date START_DATE
                        eg. 2020-02-28
  -ed END_DATE, --end-date END_DATE
                        eg. 2020-02-29
  -o OVERWRITE, --overwrite OVERWRITE
                        overwrite
```
### 4.2 simple to use
eg. 1
```shell script
sh ./bin/add_partition.sh \
 --database <database> \
 --table <table> \
 --partition-format "dt='%Y-%m-%d'" \
 --location-format "s3://xxx-region/xxxx/<database>/<table>/%Y/%m/%d" \
 --start-date 2020-03-01 \
 --end-date  2020-03-03 \
 --overwrite True
```
eg. 2
```shell script
sh ./bin/add_partition.sh \
 --database <database> \
 --table <table> \
 --partition-format "year='%Y',month='%m',day='%d'" \
 --location-format "s3://xxx-region/xxxx/<database>/<table>/%Y/%m/%d" \
 --start-date 2020-03-01 \
 --end-date  2020-03-03 \
--overwrite True
```

### 4.2 batch execute from config file (未实现)
 ```shell script
sh ./bin/add_partition.sh \
 -ac
```