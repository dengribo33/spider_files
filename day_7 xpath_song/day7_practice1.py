import requests
from lxml import etree

#爬取豆瓣电影top250

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

url ='https://www.douban.com/doulist/3936288/'


response = requests.get(url, headers=headers)

# print(response.text)

html = etree.HTML(response.text)
#连接xpath
# film_name = html.xpath('//div[@class="title"]/a/text()')
# film_abstract = html.xpath('//div[@class="abstract"]/text()')
film_data = html.xpath('//div[@class="title"]/a/text() | //div[@class="abstract"]/text()')


#取出列表中空的字符串
# film_names = [name for name in film_name if name.strip()]
# film_abstracts = [abstract for abstract in film_abstract if abstract.strip()]
film_datas = [data for data in film_data if data.strip()]

for i in film_datas:
    print(i)



