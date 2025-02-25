import requests
import os
from lxml import etree

#下载网易云音乐歌单

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

url = "https://music.163.com/playlist?id=129627424"


response = requests.get(url, headers=headers)
# print(response.text)

# 解析网页
html = etree.HTML(response.text)
#xpath解析
songs = html.xpath('//ul[@class="f-hide"]/li/a')

if not os.path.exists('songs'):
    os.mkdir('songs')


for song in songs:
    song_name = song.xpath('./text()')[0]
    id_text = song.xpath('./@href')[0].split('=')[1]

    # song_id = song.split('=')[1]

    song_url = 'https://music.163.com/song/media/outer/url?id=' + id_text

    response = requests.get(song_url, headers=headers)

    with open('songs/' + song_name + '.mp3', 'wb') as f:
        f.write(response.content)

    print(song_name + '.mp3 下载完成')


