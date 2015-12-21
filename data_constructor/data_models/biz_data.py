# coding=utf-8

from __future__ import unicode_literals
from data_constructor.db_faker.providers import BaseProvider

localized = True


class MockData(object):

    """
    DESK源和salesforce源的模拟数据集合
    :attr: TYPE_SALES: SALESFORCE OPPORTUNITY数据源中Type字段，表示客户的类型
    :attr: STAGE_NAME: SALESFORCE OPPORTUNITY数据源中StageName字段
    :attr: KH_INDUSTRY: SALESFORCE 数据源中客户行业字段
    :attr: KH_TYPE: SALESFORCE 数据源中客户类型
    :attr: STATUS: DESK CASE数据源中status字段，表示该case的状态
    :attr: RATING_TYPE: DESK CASE数据源中rating_type字段，表述该case的评分类型
    :attr: TYPE_DESK: DESK CASE数据源中type字段，表述case类型

    """

    TYPE_SALES = ["New Customer", "Existing Customer - Upgrade",
                  "OldCustomer", "null", "Existing Customer - Replacement", {}]

    STAGE_NAME = ["Qualification", "Negotiation/Review", "Closed Won", "Id. Decision Makers", "Proposal/Price Quote",
                  "Needs Analysis", "Value Proposition", "Prospecting", "Perception Analysis"]

    KH_TYPE = ["Prospect", "Customer - Channel", "Customer - Direct", {}, "Customer"]

    KH_INDUSTRY = ["Construction", "Consulting", "Energy", "Transportation", "Biotechnology",
                   "Hospitality", "Electronics", "Education", "Apparel", "Environmental",
                   "Manufacturing", "Media", "Technology", "Government"]
    LEAD_SOURCE = ["WEB", "PAPER", "A", "B", "C", {}]

    KH_RATING = ["Hot", {}, "Cold", "Warm"]

    STATUS = ["new", "open", "pending", "resolved"]

    RATING_TYPE = ["yes_no", "four_star"]

    TYPE_DESK = ["email", "phone"]


class Provider(BaseProvider):

    @classmethod
    def type_sales(cls):
        return cls.random_element(MockData.TYPE_SALES)

    @classmethod
    def stage_name(cls):
        return cls.random_element(MockData.STAGE_NAME)

    @classmethod
    def hk_type(cls):
        return cls.random_element(MockData.KH_TYPE)

    @classmethod
    def hk_industry(cls):
        return cls.random_element(MockData.KH_INDUSTRY)

    @classmethod
    def hk_rating(cls):
        return cls.random_element(MockData.KH_RATING)

    @classmethod
    def lead_source(cls):
        return cls.random_element(MockData.LEAD_SOURCE)

    @classmethod
    def status(cls):
        return cls.random_element(MockData.STATUS)

    @classmethod
    def rating_type(cls):
        return cls.random_element(MockData.RATING_TYPE)

    @classmethod
    def rating(cls, rating_type):
        """
        :param rating_type: DESK CASE数据源中rating_type字段，表述该case的评分类型
        :return: 如果type＝"yes_no" 返回0 or 3，否则为“four_star”返回｛0,1，2，3｝中一个
        """
        return cls.random_element([0, 3]) if rating_type == "yes_no" else cls.random_element([0, 1, 2, 3])

    @classmethod
    def type_desk(cls):
        return cls.random_element(MockData.TYPE_DESK)
