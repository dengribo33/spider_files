# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class DoubanMoviePipeline:
    def __init__(self):
        #创建csv文件
        self.file = open('douban_movie.csv', 'w', encoding='utf-8', newline='')
        #写入对象
        self.writer = csv.writer(self.file)
        #写入表头
        self.writer.writerow(['名称', '评分'])
        print('-------正在打开csv文件--------')

    def process_item(self, item, spider):
        self.writer.writerow(item.values())

        return item

    def __del__(self):
        self.file.close()
        print('-------csv文件已关闭--------')