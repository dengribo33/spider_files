# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

class DoubanMoviePipeline:
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['douban']
        self.collection = self.db['top250']

    def process_item(self, item, spider):
        print(item)
        self.collection.insert_one(item)
        return item


class DoubanImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        urls = ItemAdapter(item).get(self.images_urls_field, [])
        return [Request(u, meta={'image': item}) for u in urls]

    def file_path(self, request, response=None, info=None, *, item=None):
        item = request.meta.get('image')
        image_name = item['image_name']

        return f'douban_image/{image_name}.jpg'