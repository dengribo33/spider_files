import requests

# 输入要翻译的单词，360翻译
keyword = input("请输入:")

headers = {
    'Pro': 'fanyi',
    'referer': 'https://fanyi.so.com',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

url ='https://fanyi.so.com/index/search_sse'

form_data = {
    "query": "".format(keyword),
    "from": "中文",
    "to": "英文",
    "eng": "0",
    "tone": ""
}

response = requests.post(url, headers=headers, data=form_data)

result = response.json()
print(result)







