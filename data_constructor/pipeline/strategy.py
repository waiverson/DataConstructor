#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'


import xlwt, csv, requests,json, os, time
from data_constructor.conf import settings
from abc import ABCMeta, abstractmethod

import pymongo
from pymongo import MongoClient

class OutStrategy(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def out(self, data_list):
        pass


class MongoStrategy(OutStrategy):

    def __init__(self):
        address, port = settings.MONGODB
        self.dbname = settings.DBNAME
        self.collection = settings.DATATABLE
        self.conn = MongoClient(address, port)

    def get_db(self,):
        return self.conn[self.dbname]

    def get_collection(self,):

        return self.get_db()[self.collection]

    def get_max_seg(self, seg_name):
        return self.conn[self.dbname][self.collection].find().sort(seg_name, pymongo.DESCENDING).limit(1)[0]

    def get_min_seg(self, seg_name):
        return self.conn[self.dbname][self.collection].find().sort(seg_name, pymongo.ASCENDING).limit(1)[0]

    def insert(self, document):

        colet = self.get_collection()
        colet.insert(document)

    def out(self, data_list):
        self.insert(data_list)
        self.conn.close()


class CsvStrategy(OutStrategy):

    def __init__(self):
        file_name = "csv_" + str(time.time()).split('.')[0]
        csv_file = file_name + '.csv'
        self.writer = csv.writer(file(csv_file, 'wb'))
        self.offset = 0

    def out(self, data_set):
        if not self.offset:
            self.writer.writerow(data_set[0].keys())
        for data in data_set:
            self.writer.writerow(data.values())
        self.offset += len(data_set)
        try:
            self.csvfile.close()
        except Exception, ex:
            print ex


class XlsStrategy(OutStrategy):

    def __init__(self,):
        self.file_name = "xls_" + str(time.time()).split('.')[0]
        self.xls_file = self.file_name + '.xls'
        self.res_book = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.res_book.add_sheet(self.xls_file)
        self.offset = 0

        def title_style():
            return xlwt.easyxf('pattern: pattern solid, fore_colour sky_blue; '
                               'font:name Times New Roman, bold on, height 200;')

        def row_style():
            return xlwt.easyxf('font:name Consolas')

        self.title_style = title_style()
        self.row_style = row_style()

    def out(self, data_list):
        index = lambda k, title: title.index(k)
        title = data_list[0].keys()
        if not self.offset:
            for k in title:
                self.sheet.write(0, index(k, title), k, self.title_style)
        for row_no in range(0, len(data_list)):
            for col_no in range(0, len(title)):
                self.sheet.write(row_no+self.offset+1, col_no, str(data_list[row_no].values()[col_no]), self.row_style)
        self.offset += len(data_list)
        try:
            self.res_book.save(self.xls_file)
        except Exception, e:
            print str(e)

class RestAPIStrategy(OutStrategy):

    def __init__(self):
        self.username, self.password = settings.USERNAME, settings.PASSWORD
        self.url = settings.URL
        self.header = {"content-type": "application/json", "Accept": "application/json"}
        if settings.HEADER:
            self.header = settings.HEADER

    def auth(self):
        return requests.auth.HTTPBasicAuth(self.username, self.password)

    def post(self, data, auth):
        r = requests.post(self.url, data=json.dumps(data), headers=self.header, auth=auth)
        return r.status_code

    def out(self, data_list):
        auth = self.auth()
        for data in data_list:
            self.post(data, auth)
