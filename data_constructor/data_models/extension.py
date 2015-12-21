#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'


from base import BaseModel
from data_constructor.conf import settings
from data_constructor.dbhandler.pgsql2 import Pgsql

class CSVModel(BaseModel):

    def __init__(self):
        super(CSVModel, self).__init__()

    def spawn(self,):

        _collection = {"fx_ap_id": settings.CSV, "fx_org_id": 5}
        _collection.update(self.assemble())
        return _collection


class Salesforce(BaseModel):

    def __init__(self):
        super(Salesforce, self).__init__()
        self._account_name = "TEST DATA"
        self.fx_account = settings.FX_ACCOUNT_USERNAME[1]
        self._FX_SF_USER_ID = self.get_user_token()

    def get_user_token(self):

        sql = '''
              select app_user_id from core_orguserappconfig
              where  app_id = 1
              and user_id = (select id from core_orguser where user_name = '{FX_ACCOUNT_USERNAME}')
              '''.format(FX_ACCOUNT_USERNAME=self.fx_account)

        host, port, user, password, database = settings.PGSQL
        pg = Pgsql(host, port, user, password, database)
        return pg.execute_sql(sql)[0][0]

    def spawn(self,):
        # 创建来自salesforce的opportunity数据

        _collection = {"Id": self.faker.random_str(),
                        "fx_ap_userid": self._FX_SF_USER_ID,
                        "fx_ap_id": settings.SALESFORCE,
                        "IsClosed": True,
                        "IsWon": True,
                        "StageName": BaseModel.provider.stage_name(),
                        "OwnerId": self._FX_SF_USER_ID,
                        "CreatedById": self._FX_SF_USER_ID,
                        "kh_OwnerId": self._FX_SF_USER_ID,
                        "kh_Rating": BaseModel.provider.hk_rating(),
                        "fx_account_name": "TEST DATA"
        }
        _collection.update(self.assemble())
        return _collection

if __name__ == "__main__":
    print CSVModel().spawn()
    print Salesforce().spawn()