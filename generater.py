#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'

from time import time
from data_constructor.data_models.extension import CSVModel,Salesforce
from data_constructor.pipeline.processor import Processor
from data_constructor.conf import settings


class Generater(object):

    def __init__(self, model=None, processor=None):

        # 组合数据模型（model）和输出处理器（processor）
        self.batch = settings.BATCH
        self.row = settings.DATAROW
        self.model = model()
        if not model:
            self.model = Salesforce()
        self.processor = processor
        if not processor:
            self.processor = Processor.mongodb_processor('mongo')

    def produce(self,):
        for c in range(0, self.batch):
            data_list = []
            for n in xrange(self.row):
                data_list.append(self.model.spawn())
            start = time()
            self.processor.out(data_list)
            stop = time()
            print ("INSERT no.%d - datasource %s - to %s - COST TIME:%s" % (c, self.model.__class__.__name__, self.processor.name, str(stop - start)))

if __name__ == '__main__':

    # csv文件数据构造，导入到csv文件
    # Generater(CSVModel, processor=Processor.csv_processor('csv')).produce()
    # salesforce数据导入到mongo
    # Generater(Salesforce, processor=Processor.mongodb_processor('mongo')).produce()
    # csv文件构造导入到mongo
     Generater(CSVModel, processor=Processor.mongodb_processor('mongo')).produce()
    # csv文件构造，导入到xls
    # Generater(CSVModel, processor=Processor.xls_processor('xls')).produce()