import requests
from jsonpath import jsonpath
import execjs
import json

song_id = input('请输入歌曲ID：')

arg_json_data = {
    "rid": f'R_SO_4_{song_id}',
    "threadId": f'R_SO_4_{song_id}',
    "pageNo": "1",
    "pageSize": "20",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "csrf_token": "be475e793963cbd375e08b8c0c2cdc05"
}
#将字典转换为json格式
arg_string_data = json.dumps(arg_json_data)

with open('music.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
#使用call方法执行js代码
form_data = execjs.compile(js_code).call('get_data', arg_string_data)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token=be475e793963cbd375e08b8c0c2cdc05'
# form_data = {
#     'params': 'I8ulW3RXmTkaV4surSNqjTX0sNtvZ6JsNL5pyLgTXNu3f17XUVO30Swi5nGjCXqY2H1jEsDzqi+HFF6x2wIEoXk2cafOYQVKYLpTTZ3dvjcm0inrORy588wUy+NWddUd0wKUooSwFlaRa2ac79KJ9lnMWl6kHV1CFLrBTyGzyBFHXdHa6AIZmndJite1N+o2nHxAMLNuUZOAoEAJFPWaeonR9UjmLACnOGVUD1XNVv+oyPo4a0bm7lI2VrpmW1bgTZ48yGE1vUBNfyLcz/F4DSpoM+y0fZIG3lizZKbQmTBsfhwuWQgyUC9jZTH0qxti',
#     'encSecKey': 'd381dfb19be52764637d4560210b3e93cf1562e0423f6e9e8c8d8b1658d88b78b1fddefef4dd07941c0f747cd1d9546196dc5ec5595caa86eaff3342b63a280bb90c959cf263404e9c30538a99e8558a4125a513bc6fe84da65516eea596d4b969161a01484a532aed67d22c0bed87988cfb4045fdb586ae9346789c6a6c5710',
#     }
response = requests.post(url, headers=headers, data=form_data)
# print(response.json())

# name = jsonpath(response.json(), '$.data.hotComments[*].user.nickname')
# comments = jsonpath(response.json(), '$.data.hotComments[*].content')
name = jsonpath(response.json(), '$..nickname')
comments = jsonpath(response.json(), '$..content')

for name, comments in zip(name, comments):
    print('---------------------------------------------')
    print(f'评论人：{name}')
    print(f'评论内容：{comments}')









