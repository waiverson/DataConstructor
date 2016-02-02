#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'

from data_constructor.conf import settings
from data_constructor.dbhandler.pgsql2 import Pgsql
import requests, json
from abc import ABCMeta, abstractmethod

class AbsPlugin(object):

    __metaclass__ = ABCMeta

    @classmethod
    @abstractmethod
    def load(cls):
        pass

# 此插件用来调用acs服务notice接口完成从swarm_dw到分析缓存的数据转移，由于此方法为业务强挂钩的特例，所以作为plugin方式加载
class Desk51Plugin(AbsPlugin):

    @staticmethod
    def query(sql):
        host, port, user, password, database = settings.PGSQL
        pg = Pgsql(host, port, user, password, database)
        return pg.execute_sql(sql)[0][0]

    @classmethod
    def load(cls,):
        fx_account = settings.FX_ACCOUNT_USERNAME[0]
        url = settings.ACS_URL
        tag = settings.CSV
        sql = '''
            select id from core_orguser where user_name = '{FX_ACCOUNT_USERNAME}'
          '''.format(FX_ACCOUNT_USERNAME=fx_account)
        data = {'uid': Desk51Plugin.query(sql), 'ap_id': tag}
        r = requests.post(url, data=data)
        print r.text