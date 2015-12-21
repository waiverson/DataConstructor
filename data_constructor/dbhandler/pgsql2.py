#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'

import os
import psycopg2
import psycopg2.extras

class Pgsql(object):

    cur = psycopg2.extensions.cursor

    def __init__(self, host, port, user, password, database):

        conn = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
        # 创建一个字典cursor，返回数据都是字典形式
        self.cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def execute_sql(self, sql):
        self.cur.execute(sql)
        items = self.cur.fetchall()
        return items
