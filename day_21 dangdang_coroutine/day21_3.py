import time
import asyncio
from lxml import etree
from playwright.async_api import async_playwright
# 爬虫主函数
async def fetch_page(page_number):
    async with async_playwright() as playwright:
        #实例化浏览器对象，并执行为有界面模式执行
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        # 构造目标URL
        url = f'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-1?page={page_number}'

        await page.goto(url)
        # 获取当前页面的HTML源码
        html_text = await page.content()
        # 将网页html代码转换成树形结构
        html_tree = etree.HTML(html_text)
        # 使用xpath表达式来筛选书籍的节点标签元素
        book_info_list = html_tree.xpath('//ul[@class="bang_list clearfixbang_list_mode"]/li')
        # 使用循环遍历出每本书的节点信息
        for book_info in book_info_list:
        # 使用xpath表达式来筛选书籍的名称
            book_title = book_info.xpath('./div[@class="name"]/a/@title')[0]
            print(book_title)
        # 使用xpath表达式来筛选书籍的价格
            book_price =book_info.xpath('./div[@class="price"]/p[1]/span[@class="price_n"]/text()')[0]
            print(book_price)
            print(f'==================第{page_number}页的数据抓取完毕 ==================')

        await browser.close() # 关闭浏览器

# 运行多个爬虫任务
async def spider(pages):
    task_list = []
    for i in range(1, pages + 1):
        task = asyncio.create_task(fetch_page(i)) # 使用 create_task 创建任务
        task_list.append(task)
    await asyncio.wait(task_list)


if __name__ == '__main__':
    #从键盘输入抓取的页数
    pages = int(input('请输入抓取的页数：'))
    # 开始计时
    start_time = time.time()
    # 运行爬虫抓取数据
    asyncio.run(spider(pages))
    # 结束计时，并输出运行时间
    end_time = time.time()
    print('程序耗时：', end_time - start_time)
