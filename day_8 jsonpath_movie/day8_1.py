import requests
from jsonpath import jsonpath
import json
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

pages = int(input('请输入页码：'))

for page in range(pages):
    url = f'https://movie.douban.com/j/chart/top_list?type=14&interval_id=100%3A90&action=&start={page*20}&limit=20'

    response = requests.get(url, headers=headers)

    json_data = response.json()
# print(json_data)

    movie_data = jsonpath(json_data, '$..[title,regions,release_date,score]')
    print(movie_data)

    with open(f'movie/movie_data_{page + 1}.json', 'w', encoding='utf-8') as f:
        json.dump(movie_data, f, ensure_ascii=False)
        print(f'第{page+1}页数据保存成功')

    time.sleep(3)
# movies = []
# for movie in json_data:
#     movie_info = {
#         'title': movie.get('title'),
#         'regions': movie.get('regions'),
#         'release_date': movie.get('release_date'),
#         'score': movie.get('score')
#     }
#     movies.append(movie_info)
#
# print(movies)











