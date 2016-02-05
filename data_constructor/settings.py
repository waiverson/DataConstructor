#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'


FX_ACCOUNT_USERNAME = ("2215649033@qq.com",'liuweiwei5@163.com','dangwuque001@163.com', "ytuytu@qq.com", 'dangwuque@123.com')

DATATABLE = "opportunity"
             #"cases",
             #"case_history"

# 数据源标识
SALESFORCE = 1
DESK = 2
CSV = 101

# MONGODB
MONGODB = ("172.20.0.201", 27017)
DBNAME = "swarm_dw"

PGSQL = ("172.20.0.197", 5432, 'postgres', '111111', 'swarm')

# 批量插入
BATCH = 2
DATAROW = 10000

# 单位 年，创建时间相对应当前系统时间往前
YEAR = 5
# 单位 天 创建时间和解决时间的间隔
TIMEINTERVAL = 30

#ACS API
ACS_URL = 'http://172.20.0.199:16004/WEBAPI/acs/data/analysis/notice'

#RESTAPI
USERNAME = 'TOM'
PASSWORD = 'FX@123'
URL = "www.xxx.com"
