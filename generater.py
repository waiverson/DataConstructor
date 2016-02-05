#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'

from time import time
from data_constructor.data_models.extension import CSVModel, Salesforce
from data_constructor.pipeline.processor import OutProcessor, ETLProcessor
from data_constructor.pipeline.plugin import Desk51Plugin
from data_constructor.conf import settings


class Generater(object):

    def __init__(self, model=None, out_processor=None, etl_processor=None, plugin=None):

        # 组合数据模型（model）和处理器（processor）和 插件（Plugin）
        self.batch = settings.BATCH
        self.row = settings.DATAROW
        self.model = model()
        if not model:
            self.model = Salesforce()
        self.out_processor = out_processor
        if not out_processor:
            self.out_processor = OutProcessor.mongodb_processor('mongo')
        self.etl_processor = etl_processor
        if not etl_processor:
            self.etl_processor = ETLProcessor.thrid_processor('desk51')
        self.plugin = plugin
        if not plugin:
            self.plugin = Desk51Plugin

    def produce(self,):
        for c in range(0, self.batch):
            data_list = []
            for n in xrange(self.row):
                data_list.append(self.model.spawn())
            start = time()
            self.out_processor.out(data_list)
            stop = time()
            print ("INSERT no.%d - datasource %s - to %s - COST TIME:%s" % (c, self.model.__class__.__name__,
                                                                            self.out_processor.name, str(stop - start)))
        return self

    def etl(self, ):
        self.etl_processor.etl()
        return self

    def load(self,):
        self.plugin.load()
        return self


if __name__ == '__main__':

    # csv文件数据构造，导入到csv文件
    Generater(CSVModel, out_processor=OutProcessor.csv_processor('csv')).produce()
    # salesforce数据导入到mongo
    # Generater(Salesforce, out_processor=OutProcessor.mongodb_processor('mongo')).produce()
    # csv文件构造导入到mongo
    # Generater(CSVModel, out_processor=OutProcessor.mongodb_processor('mongo')).produce().load()
    # csv文件构造，导入到xls
    # Generater(CSVModel, out_processor=OutProcessor.xls_processor('xls')).produce()