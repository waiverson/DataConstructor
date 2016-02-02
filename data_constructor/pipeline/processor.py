#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'


from strategy import MongoStrategy, CsvStrategy, XlsStrategy, ThirdStrategy

class OutProcessor(object):

    def __init__(self, name, out_strategy):
        self.name = name
        self._out_strategy = out_strategy

    @staticmethod
    def mongodb_processor(name):
        return OutProcessor(name, MongoStrategy())

    @staticmethod
    def csv_processor(name):
        return OutProcessor(name, CsvStrategy())

    @staticmethod
    def xls_processor(name):
        return OutProcessor(name, XlsStrategy())

    def out(self, data_list):
        self._out_strategy.out(data_list)

class ETLProcessor(object):

    def __init__(self, name, etl_strategy):
        self.name = name
        self._etl_strategy = etl_strategy

    @staticmethod
    def thrid_processor(name):
        return ETLProcessor(name, ThirdStrategy())




