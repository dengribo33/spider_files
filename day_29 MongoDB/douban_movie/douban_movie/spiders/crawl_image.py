import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DoubanMovieItem

class CrawlImageSpider(CrawlSpider):
    name = "crawl_image"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    rules = (
        #电影详情页
        Rule(LinkExtractor(allow=r'^https://movie.douban.com/subject/\d+/'),callback='parse_item', follow=False),
        #翻页标签
        Rule(LinkExtractor(restrict_xpaths='//span[@class="next"]/a'),follow=True),
    )

    def parse_item(self, response):
        items = DoubanMovieItem()
        #海报url和名字
        image_url = response.xpath('//div[@id="mainpic"]/a/img/@src').get()
        image_name =response.xpath('//span[@property="v:itemreviewed"]/text()').get()
        #文件名称不能有英文冒号
        image_name = image_name.replace(': ', '：')
        #传递给items
        items['image_urls'] = [image_url]
        items['image_name'] = image_name
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        return items
