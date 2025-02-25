import requests
import re
import os

url = 'https://www.huya.com/g/2168'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

if not os.path.exists('screenshot'):
    os.mkdir('screenshot')

response = requests.get(url, headers=headers)
# print(response.text)
obj = '"sIntroduction":"(.*?)".*?"sScreenshot":"(.*?)","iIsSecret"'
result_list = re.findall(obj, response.text)
# print(result_list)
#赋值的方式
# for name, screenshot_url in result_list:
    # print(name, screenshot_url)
#通过索引的方式
for i in result_list:
    name = i[0]
    screenshot_url = i[1]
    response = requests.get(screenshot_url, headers=headers)
    with open(f'screenshot/{name}.jpg', 'wb') as f:
        f.write(response.content)
    print(f'{name}.jpg 保存成功')