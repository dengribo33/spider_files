import requests  # 数据请求模块 pip install requests (第三方模块)
import pprint  # 格式化输出模块 内置模块 不需要安装
import re  # 正则表达式
import json

#数据请求
def get_response(html_url):
    # 用python代码模拟浏览器
    # headers 把python代码进行伪装
    # user-agent 浏览器的基本标识
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    # 用代码直接获取的 一般大多数都是直接 cookie
    response = requests.get(url=html_url, headers=headers)
    return response

# 获取视频标题以及url地址
def get_video_info(video_id):
    html_url = f'https://liveapi.huya.com/moment/getMomentContent?videoId={video_id}&uid=&_=1634127164373'
    response = get_response(html_url)
    title = response.json()['data']['moment']['title'] # 视频标题
    video_url = response.json()['data']['moment']['videoInfo']['definitions'][0]['url']
    video_info = [title, video_url]
    return video_info

#获取视频id
def get_video_id(html_url):
    html_data = get_response(html_url).text
    result = re.findall('<script> window.HNF_GLOBAL_INIT = (.*?) </script>', html_data)[0]
    # 需要把获取的字符串数据, 转成json字典数据
    json_data = json.loads(result)['videoData']['videoDataList']['value']
    # json_data 列表和字典操作 里面元素是字典
    # print(json_data)
    video_ids = [i['vid'] for i in json_data]  # 列表推导式
    # lis = []
    # for i in json_data:
    #     lis.append(i['vid'])
    # print(video_ids)
    # print(type(json_data))
    return video_ids

# 保存视频
def save(title, video_url):
    # 保存数据, 也是还需要对于播放地址发送请求的
    # response.content 获取响应的二进制数据
    video_content = get_response(html_url=video_url).content
    new_title = re.sub(r'[\/:*?"<>|]', '_', title)
    # 'video\\' + title + '.mp4' 文件夹路径以及文件名字 mode 保存方式 wb二进制保存方式
    with open('video\\' + new_title + '.mp4', mode='wb') as f:
        f.write(video_content)
        print('保存成功: ', title)

# 目光所至 我皆可爬
def main(html):
    video_ids = get_video_id(html_url=html)
    for video_id in video_ids:
        video_info = get_video_info(video_id)
        save(video_info[0], video_info[1])

if __name__ == '__main__':
    # get_video_info('589462235')
    video_info = get_video_info('589462235')
    save(video_info[0], video_info[1])
    for page in range(1, 6):
        print(f'正在爬取第{page}页的数据内容')
        # python基础入门课程 第一节课 讲解的知识点 字符串格式化方法
        url = f'https://v.huya.com/g/all?set_id=31&order=hot&page={page}'
        main(url)



