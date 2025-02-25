import scrapy
from jsonpath import jsonpath
import re

class Fanyi360Spider(scrapy.Spider):
    name = "fanyi360"
    allowed_domains = ["fanyi.so.com"]
    # start_urls = ["https://fanyi.so.com/"]
    #重写start_requests方法

    def start_requests(self):
        url = "https://fanyi.so.com/index/search_sse"

        keyword = input("请输入要翻译的单词或句子: ")

        form_data = {
            "query": f"{keyword}",
            "from": "英文",
            "to": "中文",
            "eng": "1",
            "tone": "",
        }
        yield scrapy.FormRequest(url, formdata=form_data, callback=self.parse)


    def parse(self, response):
        # print(response.text)
        pattern = r'"content":"(.*?)"'
        result = re.findall(pattern, response.text)[0]
        print(f"翻译结果: {result}")

        pass
