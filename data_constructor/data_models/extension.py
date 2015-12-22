#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'


from base import BaseModel


class CSVModel(BaseModel):

    def __init__(self):
        super(CSVModel, self).__init__()
        sql = '''
              select org_id from core_orguser where user_name = '{FX_ACCOUNT_USERNAME}'
              '''.format(FX_ACCOUNT_USERNAME=self.fx_account)
        self._fx_org_id = self.query(sql)

    def spawn(self,):

        _collection = {"fx_ap_id": BaseModel.settings.CSV, "fx_org_id": self._fx_org_id}
        _collection.update(self.assemble())
        return _collection


class Salesforce(BaseModel):

    def __init__(self):
        super(Salesforce, self).__init__()
        self._account_name = "TEST DATA"
        sql = '''
              select app_user_id from core_orguserappconfig
              where  app_id = 1
              and user_id = (select id from core_orguser where user_name = '{FX_ACCOUNT_USERNAME}')
              '''.format(FX_ACCOUNT_USERNAME=self.fx_account)
        print sql
        self._FX_SF_USER_ID = self.query(sql)

    def spawn(self,):
        # 创建来自salesforce的opportunity数据

        _collection = {"Id": self.faker.random_str(),
                        "fx_ap_userid": self._FX_SF_USER_ID,
                        "fx_ap_id": BaseModel.settings.SALESFORCE,
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