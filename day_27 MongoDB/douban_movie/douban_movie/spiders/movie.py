import scrapy

class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        titles_list = response.xpath('//div[@class="hd"]/a/span[1]/text()').getall()
        scores_list = response.xpath('//span[@class="rating_num"]/text()').getall()
        urls_list = response.xpath('//div[@class="hd"]/a/@href').getall()
        # print(titles_list, scores_list, urls_list)
        #筛选出电影的名称、评分、链接并导入到字典中
        for title, score, url in zip(titles_list, scores_list, urls_list):
            items = {'title': title,'score': score,'url': url}

            #将电影信息url发送给parse_url函数进行解析，并将item传递给parse_url函数
            yield scrapy.Request(url, callback=self.parse_url, meta={'data': items})
        #当前页处理完毕，获取下一页的链接并发送请求
        next_page = response.xpath('//span[@class="next"]/a/@href').get()
        yield response.follow(next_page, callback=self.parse)

    #解析电影详情页面
    def parse_url(self, response):
        # 筛选电影的简介
        text_list =response.xpath('//span[@property="v:summary"]/text()').getall()
        # print(text_list)
        #将列表转换为字符串，并将空格、换行符、全角空格替换为空格
        text = ''.join(text_list)
        text = text.replace('\n', '').replace(' ', '').replace('\u3000', '')
        # print(text)
        # 将传递过来的item字典提取出来
        items = response.meta.get('data')
        # 将电影简介添加到item字典中
        items['text'] = text
        # print(items)
        yield items
