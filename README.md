# athena-operation

## 1. clone
  > * git clone xxx
## 2. env config
  > * export AWS_ACCESS_KEY_ID=xxx
  > * export AWS_SECRET_ACCESS_KEY=xxx
## 3. config
  > * athena_s3_result_tmp_path
## 4. use
### 4.1 show help
  > * sh ./bin/add_partition.sh --help
```text
usage: athena_opertation.py [-h] [-ac ALL_CONFIG] [-d DATABASE] [-t TABLE]
                            [-p PARTITIONS] [-l LOCATION] [-o OVERRIDE]

athena operation

optional arguments:
  -h, --help            show this help message and exit
  -ac ALL_CONFIG, --all-config ALL_CONFIG
                        load partition info from config file
  -d DATABASE, --database DATABASE
                        database
  -t TABLE, --table TABLE
                        table
  -p PARTITIONS, --partitions PARTITIONS
                        k1=v1,k2=v2,k3=v3
  -l LOCATION, --location LOCATION
                        location
  -o OVERRIDE, --override OVERRIDE
                        override
```
### 4.2 simple to use
 ```shell script
sh ./bin/add_partition.sh \
 --database <database> \
 --table <table> \
 --partitions "dt='2020-01-16'" \
 --location "s3://xxx-region/xxxx/2020/01/16" \ 
 --override
```
### 4.2 batch execute from config file
 ```shell script
sh ./bin/add_partition.sh \
 -ac
```