import time
import os
import asyncio
import aiohttp
from lxml import etree
from fake_useragent import FakeUserAgent

#定义并发数为10
CONCURRENCY = 10

#限制并发数
semaphore = asyncio.Semaphore(CONCURRENCY)

#定义请求头
headers = {'user-agent':FakeUserAgent().random}

#发送请求函数
async def request_index():
    url = 'https://sc.chinaz.com/tupian/xiangcuntianyuan.html'
    #实例化session对象
    async with aiohttp.ClientSession() as session:
        async with await session.get(url,headers=headers) as response:
            #获取响应的文本数据
            response_text = await response.text()
            #解析响应的html数据
            html = etree.HTML(response_text)
            #获取图片链接和标题
            img_urls = html.xpath('//div[@class="item"]/img[@class="lazy"]/@data-original')
            titles = html.xpath('//div[@class="item"]/img[@class="lazy"]/@alt')
            #定义一个列表，用于保存图片的下载任务
            urls = []
            for i in img_urls:
                #为每个图片链接添加请求头
                img_url = 'https:' + i
                urls.append(img_url)
            #打包成一个字典，用于保存图片的标题和下载链接
            results = dict(zip(titles, urls))
            return results
#定义下载图片函数
async def download_img(title, url):
    #控制并发数为10
    async with semaphore:
        #实例化session对象
        async with aiohttp.ClientSession() as session:
            async with await session.get(url,headers=headers) as response:
                #获取响应的二进制数据
                content = await response.read()

                #保存图片到本地
                with open(f'./images/{title}.jpg', 'wb') as f:
                    f.write(content)
                    print(title+'下载完成')
            #控制下载速度
            await asyncio.sleep(1)

#定义主函数
async def main():
    #获取图片链接和标题
    images_dict = await request_index()

    #创建异步任务列表
    task_list = []
    for title, url in images_dict.items():
        #创建异步任务
        task = asyncio.ensure_future(download_img(title, url))
        task_list.append(task)
    #等待异步任务完成
    await asyncio.wait(task_list)

if __name__ == '__main__':
    if not os.path.exists('./images'):
        os.mkdir('./images')

    start_time = time.time()
    #实例化事件循环对象loop
    loop = asyncio.get_event_loop()
    #运行异步任务
    loop.run_until_complete(main())

    end_time = time.time()
    print(f'下载完成，用时{end_time-start_time}秒')































