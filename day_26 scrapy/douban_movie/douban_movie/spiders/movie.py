import scrapy
class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["movie.douban.com"] # 爬虫的抓取域名范围
    start_urls = ["https://movie.douban.com/top250"] # 爬虫的起始URL
    # response 就是发起请求后的响应
    def parse(self, response):
        title_list = response.xpath('//a/span[@class="title"][1]/text()').getall()
        # print(title_list)
        score_list = response.xpath('//span[@class="rating_num"]/text()').getall()
        # print(score_list)
        for title, score in zip(title_list, score_list):
            #将title和score打包成字典
            item = {
                "title": title,
                "score": score
            }
            yield item