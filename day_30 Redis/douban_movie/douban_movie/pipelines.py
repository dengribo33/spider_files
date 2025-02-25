# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class DoubanMoviePipeline:
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['douban']
        self.collection = self.db['scrapy_redis']

    def process_item(self, item, spider):
        print(item)
        self.collection.insert_one(item)
        return item