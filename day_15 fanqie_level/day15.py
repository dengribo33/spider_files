import requests
import re
from lxml import etree
from fontTools.ttLib import TTFont
import ddddocr
from PIL import Image, ImageDraw, ImageFont

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

url = 'https://fanqienovel.com/reader/7276663560427471412'

response = requests.get(url, headers=headers)
# print(response.text)
#筛选小说内容
html = etree.HTML(response.text)
message = html.xpath('//div[@class="muye-reader-content noselect"]/div/p/text()')
# print(message)
#获取字体下载地址
font_re = r'src:url\((.*?)\)format\("woff2"\)'
font_url = re.findall(font_re, response.text)[0]
# print(font_url)
#下载并保存字体文件
response = requests.get(font_url, headers=headers)
# print(response.text)
with open('font.woff2', 'wb') as f:
    f.write(response.content)
#读取字体文件，读取cmap数据
font = TTFont('font.woff2')
cmap = font.getBestCmap()
#码点值与符号的映射字典
map_key = {}
#识别
ocr = ddddocr.DdddOcr()

for key in cmap:
    #创造一张空白图片，创造一个绘画对象，提取字体文件的笔画并绘制到图片上
    img = Image.new('RGB', (150, 150), color='white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('font.woff2', 50)
    draw.text((50, 50), chr(key), font=font, fill='black')
    #识别图片上的文字并判断是否识别成功
    result = ocr.classification(img)
    # print(result)
    if result:
        map_key[key] = result
    else:
        print(f"{key}.jpg")

print(map_key)

#遍历小说内容，得到单个字符，用符号还原后的码点值从字典中取值，判断是否为加密文字
for message_line in message:
    for word in message_line:
        # 根据字符的 ASCII 值从映射键中获取数据，ord() 函数获取字符的整数码点值
        data = map_key.get(ord(word))
        # 如果存在数据，则输出，否则输出原字符
        if data is not None:
            print(data, end='')
        else:
            print(word, end='')

    print()

















