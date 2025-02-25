import requests

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}


url = 'https://www.baidu.com/'


response = requests.get(url,headers=headers)

response.encoding = 'utf-8'


with open('test.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
