import  time
import asyncio
from lxml import etree
from playwright.async_api import async_playwright

async def feach_page(pages):
    async with async_playwright() as playwright:
        #实例化浏览器对象
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        #url
        url = f'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-{pages}'
        await page.goto(url)
        #获取当前html内容
        html =await page.content()
        #解析html
        html_tree = etree.HTML(html)
        #获取书籍节点标签元素
        books_info_list = html_tree.xpath('//ul[@class="bang_list clearfix bang_list_mode"]/li')

        for book_info in books_info_list:
            book_name = book_info.xpath('./div[@class="name"]/a/@title')[0]
            print(book_name)
            book_price = book_info.xpath('./div[@class="price"]/p[1]/span[@class="price_n"]/text()')[0]
            print(book_price)

        print(f'第{pages}页爬取完成--------------------------------------------')

        await browser.close()

#运行多个爬虫任务
async def spider(pages):
    tasks_list = []
    for i in range(1,pages+1):
        task = asyncio.create_task(feach_page(i)) #创建任务
        tasks_list.append(task)

    await asyncio.wait(tasks_list)

if __name__ == '__main__':
    pages = int(input('请输入需要爬取的页数：'))
    start = time.time()

    asyncio.run(spider(pages))

    end = time.time()
    print(f'爬取完成，共耗时{end-start}秒')







