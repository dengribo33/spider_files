import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

url = 'https://sc.chinaz.com/tupian/xiangcuntianyuan.html'


response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
print(response.text)

html = etree.HTML(response.text)

name = html.xpath('//div[@class="item"]/img[@class="lazy"]/@alt')
img = html.xpath('//div[@class="item"]/img[@class="lazy"]/@data-original')
print(name)
print(img)
