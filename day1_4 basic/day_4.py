import requests

# 输入要翻译的单词，360翻译
keyword = input("请输入:")

headers = {
    'Pro': 'fanyi',
    'referer': 'https://fanyi.so.com',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

url = 'https://fanyi.so.com/index/search'


form_data = {
    "eng": "study_day",
    "validate": "",
    "ignore_trans": "0",
    "query": "{}".format(keyword),
}
response = requests.post(url, headers=headers,data=form_data)

d = response.json()
print(d['data']['fanyi'])



