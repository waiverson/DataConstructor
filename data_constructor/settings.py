#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'


FX_ACCOUNT_USERNAME = ('liuweiwei5@163.com','dangwuque001@163.com',"2215649033@qq.com", "ytuytu@qq.com", 'dangwuque@123.com')

DATATABLE = "opportunity"
             #"cases",
             #"case_history"

# 数据源标识
SALESFORCE = 1
DESK = 2
CSV = 101

# MONGODB
MONGODB = ("172.20.0.215", 27017)
DBNAME = "swarm_dw7"

PGSQL = ("172.20.0.216", 5432, 'postgres', '111111', 'swarm')

# 批量插入
BATCH = 1
DATAROW = 10000

# 单位 年，创建时间相对应当前系统时间往前
YEAR = 5
# 单位 天 创建时间和解决时间的间隔
TIMEINTERVAL = 30

#RESTAPI
USERNAME = 'TOM'
PASSWORD = 'FX@123'
URL = "www.xxx.com"
