#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'


from strategy import MongoStrategy, CsvStrategy, XlsStrategy

class Processor(object):

    def __init__(self, name, out_strategy):
        self.name = name
        self._out_strategy = out_strategy

    @staticmethod
    def mongodb_processor(name):
        return Processor(name, MongoStrategy())

    @staticmethod
    def csv_processor(name):
        return Processor(name, CsvStrategy())

    @staticmethod
    def xls_processor(name):
        return Processor(name, XlsStrategy())

    def out(self, data_list):
        self._out_strategy.out(data_list)





