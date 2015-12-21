#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'

FX_USER_ID = (("00528000001X1unAAC", "23910436"),
              )


FX_ACCOUNT_USERNAME = ("2215649033@qq.com", "ytuytu@qq.com")

DATATABLE = "opportunity"
             #"cases",
             #"case_history"

# 数据源标识
SALESFORCE = 1
DESK = 2
CSV = 101

# MONGODB
MONGODB = ("172.20.0.214", 27017)
DBNAME = "swarm_dw"

PGSQL = ("172.20.0.214", 5432, 'postgres', 'postgres', 'swarm')

# 批量插入
BATCH = 1
DATAROW = 100

# 单位天 创建时间和解决时间的间隔
TIMEINTERVAL = 30

#RESTAPI
USERNAME = 'TOM'
PASSWORD = 'FX@123'
URL = "www.xxx.com"
