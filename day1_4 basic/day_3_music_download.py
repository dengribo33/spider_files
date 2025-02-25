import requests

# 从键盘输入歌曲的名字
music_name = input('请输入歌曲的名字：')

# 从键盘输入歌曲的ID
music_id = input('请输入歌曲的ID：')

# 定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

# 下载音乐的请求网址（不完整的）
url = 'https://music.163.com/song/media/outer/url?id=' + music_id


# 发起网络请求
response = requests.get(url, headers=headers)

# 将请求的结果保存成html文件
with open(f'{music_name}.mp3', 'wb') as file:
    file.write(response.content)










