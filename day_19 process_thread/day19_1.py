import requests
import re
import os
import time
import multiprocessing
import threading

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url = 'https://www.huya.com/g/2168'

response = requests.get(url, headers=headers)
# print(response.text)
#获取标题和图片链接并存入列表中
obj = '"sIntroduction":"(.*?)".*?"sScreenshot":"(.*?)","iIsSecret"'
result_list = re.findall(obj, response.text)
# print(result_list)
url_list = []
name_list = []
for i in result_list:
    name_list.append(i[0])
    url_list.append(i[1])

#定义下载图片名字和链接的函数
def request_img(img_name, img_url):
    response = requests.get(img_url, headers=headers)
    with open(f'./images/{img_name}.jpg', 'wb') as f:
        f.write(response.content)
        print(f'{img_name}.jpg 下载完成')

#定义多进程请求方法
def multi_process_request():
    # 创建进程池，指定最大进程数为3,计算时间
    start_time = time.time()
    pool = multiprocessing.Pool(3)
    for name,url in zip(name_list,url_list):
        pool.apply_async(request_img, args=(name, url,))
    # 关闭进程池，不再接受新任务
    pool.close()
    # 等待所有进程执行完毕
    pool.join()
    end_time = time.time()
    print(f'多进程下载完成，用时{end_time-start_time}秒')

#定义多线程请求方法
def multi_thread_request():
    # 程序开始计时
    start_time = time.time()
    #创建线程列表
    thread_list = []
    for name,url in zip(name_list,url_list):
        # 创建多个线程去请求数据
        t = threading.Thread(target=request_img, args=(name, url,))
        thread_list.append(t)
        t.start()
    # 等待所有线程执行完毕
    for t in thread_list:
        t.join()
    # 程序结束计时
    end_time = time.time()
    # 输出程序运行所花费的时长
    print(f'多线程下载完成，用时{end_time-start_time}秒')

if __name__ == '__main__':
    if not os.path.exists('./images'):
        os.mkdir('./images')

    multi_process_request()
    multi_thread_request()


#定义单进程请求方法
# def single_process_request():
#     start_time = time.time()
#     for url, name in zip(img_list, title_list):
#         request_img(url, name)
#     end_time = time.time()
#     print(f'单进程下载完成，用时{end_time-start_time}秒')


# 定义单线程请求方法
# def single_thread_request():
#     # 程序开始计时
#     start_time = time.time()
#     # 循环遍历出每个名字和链接
#     for name, url in zip(name_list, url_list):
#         # 调用函数下载
#             request_img(name, url)
#     # 程序结束计时
#     end_time = time.time()
#     # 输出程序运行所花费的时长
#     print(f'普通请求时，程序运行共计：{end_time - start_time}秒')



















