#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'


from data_constructor.conf import settings
from data_constructor.db_faker.factory import Factory
from data_constructor.data_models.utils import Utils
from data_constructor.data_models.biz_data import Provider
from data_constructor.dbhandler.pgsql2 import Pgsql

class BaseModel(object):

    provider = Provider
    settings = settings

    def __init__(self):

        self.interval = settings.TIMEINTERVAL * 24 * 60 * 60  # 换算成秒
        self.year = settings.YEAR
        self.fx_account = settings.FX_ACCOUNT_USERNAME[0]
        self.base_columns = [
                "fiscal_year",
                "kh_Name",
                "CreatedDate",
                "CloseDate",
                "Amount",
                "LeadSource",
                "kh_Type",
                "kh_Industry",
                "kh_BillingAddress",
                "kh_AnnualRevenue",
                "Name",
                "Type",
                "fx_campaign_name",
                "fx_owner_name"
            ]

        self.faker = Factory.create()

    def query(self,sql):
        host, port, user, password, database = settings.PGSQL
        pg = Pgsql(host, port, user, password, database)
        try:
            rs = pg.execute_sql(sql)[0][0]
            return rs
        except IndexError,e:
            print e
            return 'None'

    def assemble(self,):
        # 构造基础的数据集

        _created_time = Utils.created_time(self.faker, self.year)
        _end_time = Utils.end_time(_created_time, interval=self.interval)

        values = [2016,  #fiscal_year
                     self.faker.company(), # kh_name
                     _created_time, # createdate
                     _end_time, #closedate
                     self.faker.pyfloat(left_digits=6, right_digits=2, positive=True), #amount
                     BaseModel.provider.lead_source(), #leadsource
                     BaseModel.provider.hk_type(), #kh_type
                     BaseModel.provider.hk_industry(), #kh_industry
                     {}, # kh_billingaddress
                     self.faker.pyfloat(left_digits=5, right_digits=2, positive=True), #kh_annualrevenue
                     self.faker.company(), #name
                     BaseModel.provider.type_sales(),    #Type
                     {}, #fx_campaign_name
                     "TOM", #fx_owner_name
            ]

        return Utils.to_dict(self.base_columns, values)


