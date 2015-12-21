# coding=utf-8

from ..db_faker.providers.date_time import *
from datetime import datetime
import random


class Utils(object):

    _SEQ = 0

    @classmethod
    def created_time(cls, faker):

        return faker.date_time_between_dates(datetime_start=datetime(2010, 8, 1), datetime_end=datetime(2015, 11, 1))

    @classmethod
    def end_time(cls, created_time, interval=5184000):
        """
        :param: created_time: DateTime对象，创建时间。
        :param: interval: 创建时间于结束时间的间隔 ，单位：s。5184000=2 month
        :return: 结束时间
        """

        return datetime.fromtimestamp(datetime_to_timestamp(created_time) + random.randint(0, interval))

    @classmethod
    def get_inc_seq(cls, init_seq=0):
        """
        :param: collection: mongodb collection name。先获取mongodb中已存在的id值，目前暂不实现
        :return: current seq of collection
        """
#        if not cls._SEQ and init_seq:
#           cls._SEQ = init_seq
        cls._SEQ += 1
        return cls._SEQ

    @classmethod
    def to_dict(cls, keys, values):
        """
        :param keys: 返回数据集的字段名
        :param values: 返回数据集的字段值
        :return: 返回数据集
        """
        return dict(zip(keys, values))
