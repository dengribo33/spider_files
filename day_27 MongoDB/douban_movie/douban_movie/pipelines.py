# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class DoubanMoviePipeline:
    #连接mongodb数据库集合中的文档
    def __init__(self):
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.client['douban']
        self.collection = self.db['movies_info']

    def process_item(self, item, spider):
        print(item)
        #将item中的数据插入mongodb数据库集合中
        self.collection.insert_one(item)
        return item

