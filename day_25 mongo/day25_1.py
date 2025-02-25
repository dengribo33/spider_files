import pymongo
import jsonpath
import requests

numbers = int(input("请输入要爬取的电影数量："))

url = f'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit={numbers}&page_start=0'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
response = requests.get(url, headers=headers)

movies_title = jsonpath.jsonpath(response.json(), '$..title')
# print(movies_title)
movies_url = jsonpath.jsonpath(response.json(), '$..url')
# print(movies_url)

movie_list = []

for title,url in zip(movies_title,movies_url):
    # print(title,url)
    #定义一个字典，用来存储电影信息
    movies_dict = {"title":title,"url":url}
    movie_list.append(movies_dict)

# print(movie_list)
#建立连接
client = pymongo.MongoClient()
#创造数据库
db = client['douban']
#创造集合
collection = db['movies']
#插入数据
collection.insert_many(movie_list)
#查询数据
result = collection.find()

for i in result:
    print(i)








