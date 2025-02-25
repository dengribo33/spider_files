import time
import re
import requests
from DrissionPage import ChromiumPage
from lxml import etree
from fontTools.ttLib import TTFont

# 打开网页
page = ChromiumPage()
page.get("https://www.qidian.com/rank/yuepiao/")
time.sleep(2)

# 获取网页源码
html = page.html
tree = etree.HTML(html)

# 获取书名列表
page_name_list= tree.xpath("//h2/a/text()")
print(page_name_list)

#获取月票数
page_ticket_list = tree.xpath("//span/span/text()")
print(page_ticket_list)

# 存放密文字符串
book_ticket_list = []

for book_ticket_text in page_ticket_list:
    string = ''.join(f"{ord(i)};" for i in book_ticket_text)
    book_ticket_list.append(string)
print(book_ticket_list)

#字体链接
font_url = tree.xpath("//span/style/text()")[0]
print(font_url)

# 下载字体文件
font_file = r"format\('eot'\); src: url\('(.*?)'\) format\('woff'\)"
font_file1 = re.findall(font_file, font_url)[0]
print(font_file1)

# 保存字体文件
response = requests.get(font_file1)
with open("font.woff", 'wb') as f:
    f.write(response.content)

# 解析字体文件
font_obj = TTFont("font.woff")
cmap = font_obj.getBestCmap()
print(cmap)

# 定义一个用户替换的字典
number = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0',
    'period': '.'
}

#替换英文数字为阿拉伯数字
for i in cmap:
    for j in number:
        if cmap[i] == j:
            cmap[i] = number[j]
print(cmap)

for book_name, book_ticket in zip(page_name_list, book_ticket_list):
    number_list = book_ticket.split(';')
    number_list1 = list(filter(None, number_list))
    # number_list = re.findall(r'\d+', book_ticket)
    # print(number_list1)
    number_str = ''

    for number in number_list1:
        num = cmap.get(int(number))
        # print(num)
        number_str += num

    print(f"书名：{book_name}, 月票数：{number_str}")


page.quit()













