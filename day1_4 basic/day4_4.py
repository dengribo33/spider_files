import os
import requests
from moviepy.editor import VideoFileClip    # 这个是用于读取ts文件的方法
from moviepy.editor import concatenate_videoclips   # 这个方法用于合并所有的ts文件


# 定义获取视频ts片段的函数
def get_video_ts():
    # 定义请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    # 循环下载每个ts文件
    for i in range(30):
        # 定义请求的网址
        ts_url = f'https://play-tx-ugcpub.douyucdn2.cn/live/high_146650620240418145505-upload-25ed/transcode_146650620240418145505-upload-25ed_121264_00000{i:02}.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108'
        # print(ts_url)

        # 发起网络请求,获取ts文件数据
        response = requests.get(ts_url, headers=headers)

        # 将ts视频片段数据保存成ts文件
        with open(f'./videos/transcode_00000{i:02}.ts', 'wb') as file:
            file.write(response.content)
        print(f'00000{i:02}.ts 下载成功')


# 定义合并ts文件
def merge_ts_file():
    # 读取videos文件夹中所有的ts文件名称
    file_name_list = os.listdir('videos')
    print(file_name_list)

    # 定义一个列表用于存放所有的ts文件
    clip_list = []

    # 循环读取所有的ts文件
    for file_name in file_name_list:
        # 读取每个ts文件
        clip = VideoFileClip('./videos/' + file_name)
        # 将每个ts文件追加到列表中
        clip_list.append(clip)
        print(file_name, '读取完毕')

    # 合并所有的ts文件
    final_clip = concatenate_videoclips(clip_list)

    # 将合并后的文件转换成mp4文件
    final_clip.write_videofile('视频.mp4')


if __name__ == '__main__':
    # 调用视频合并函数
    merge_ts_file()


"""
https://play-tx-ugcpub.douyucdn2.cn/live/high_146650620240418145505-upload-25ed/
transcode_146650620240418145505-upload-25ed_121264_0000029.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108

transcode_146650620240418145505-upload-25ed_121264_0000000.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000001.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000002.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000003.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000004.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000005.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000006.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000007.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000008.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000009.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000010.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000011.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000012.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000013.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000014.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000015.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000016.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000017.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000018.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000019.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000020.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000021.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000022.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000023.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000024.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000025.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000026.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000027.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000028.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
transcode_146650620240418145505-upload-25ed_121264_0000029.ts?cdn=tx&ct=web&d=90380569ae90cb825e46653000011701&exper=0&nlimit=5&pt=2&sign=dcdf2dae625e301e20b2d42dae880131&tlink=66f2d95d&tplay=66f365fd&u=0&us=90380569ae90cb825e46653000011701&vid=40996108
"""