#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'


FX_ACCOUNT_USERNAME = ("xxx@qq.com",'aaa@163.com','ccc@163.com', "bbb@qq.com", 'ddd@123.com')

DATATABLE = "opportunity"
             #"cases",
             #"case_history"

# 数据源标识
SALESFORCE = 1
DESK = 2
CSV = 101

# MONGODB
MONGODB = ("172.20.0.xxx", 27017)
DBNAME = "xxx"

PGSQL = ("172.20.0.xxx", 5432, 'postgres', '111111', 'xxx')

# 批量插入
BATCH = 2
DATAROW = 10000

# 单位 年，创建时间相对应当前系统时间往前
YEAR = 5
# 单位 天 创建时间和解决时间的间隔
TIMEINTERVAL = 30

#ACS API
ACS_URL = 'rest_uri'

#RESTAPI
USERNAME = 'TOM'
PASSWORD = 'FX@123'
URL = "www.xxx.com"
