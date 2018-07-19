# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import xlwt
import csv
"""
create table bole_list(
    title varchar(150),
    thumb_url varchar(255),
    date varchar(30),
    tag varchar(10),
    summary text,
    detail_url varchar(150));
    
"""
class Homework0719Pipeline(object):
    base_sql = "insert into bole_list values('%s', '%s', '%s', '%s', '%s', '%s');"
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", user="root", password="root", charset="utf8", db="bole")
        self.cursor = self.conn.cursor()

    def spider_close(self):
        self.conn.close()

    def process_item(self, item, spider):
        sql = self.base_sql % (item["title"], item["thumb_url"], item["date"], item["tag"], item["summary"], item["detail_url"])
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
        return item
class XlsPipeline(object):
    def __init__(self):
        self.wbk = xlwt.Workbook()
        self.sheet = self.wbk.add_sheet("xls", cell_overwrite_ok=True)
    def process_item(self, item, spider):
        col_num = 0
        for key, value in item.items():
            self.sheet.write(item["curr_index"], col_num, value)
            col_num += 1
        self.wbk.save("excel.xls")
        return item
class CsvPipeline(object):
    def process_item(self, item, spider):
        with open("./csv.csv", "a", newline="") as csv_file:
            write = csv.writer(csv_file)
            write.writerow(list(item.values()))
        return item
