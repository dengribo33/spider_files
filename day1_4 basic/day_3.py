import requests

#params传参请求360搜索

keyword = input("请输入:")

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

url = 'https://www.so.com/s?'

params = {
    "ie": "utf-8",
    "fr": "home_placeholder",
    "src": "home_placeholder",
    "ssid": "5e36de57f5f744eeb2ca0c4af3710fef",
    "sp": "ae2",
    "cp": "030ae2000a",
    "nlpv": "placeholder_base_zc_61",
    "q": keyword
}

response = requests.get(url, headers=headers, params=params)

with open(f'360-{keyword}.html', 'wb') as f:
    f.write(response.content)



