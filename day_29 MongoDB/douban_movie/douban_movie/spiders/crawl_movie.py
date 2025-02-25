import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrawlMovieSpider(CrawlSpider):
    name = "crawl_movie"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    rules = (
        #电影详情页链接
        Rule(LinkExtractor(allow=r'^https://movie.douban.com/subject/\d+/'),
callback='parse_item', follow=False),
        #点击下一页链接
        Rule(LinkExtractor(restrict_xpaths='//span[@class="next"]/a'),
follow=True),
    )

    def parse_item(self, response):
        title = response.xpath('//span[@property="v:itemreviewed"]/text()').get()
        score = response.xpath('//strong[@property="v:average"]/text()').get()
        url = response.url
        text_list = response.xpath('//span[@property="v:summary"]/text()').getall()
        text = ''.join(text_list)
        text = text.replace('\n', '').replace(' ', '').replace('\u3000', '')
        print(text)
        item = {'title': title, 'score': score, 'url': url, 'text': text}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        return item
