import csv  # 这个库不需要安装
import time
import random
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

def get_book_info(pages):
    # 实例化浏览器对象，打开对应的网页并设置窗口最大化
    driver = webdriver.Edge()
    driver.get('http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-1')
    driver.maximize_window()

    # 定义一个空列表用于存放所有筛选出来的书籍信息
    book_data_list = []

    for page in range(pages):
        # 设置页面的滚动下滑，从而保证整页数据加载完毕
        for i in range(1, 6):
            # 随机等待1-3秒
            random_num = random.randint(1, 3)
            time.sleep(random_num)
            # 分批次下滑滚动
            random_range = random.randint(500, 1000)
            driver.execute_script(f'window.scrollTo(0, {i * random_range});')

        # 获取网页源代码
        html_data = driver.page_source

        # 将网页html代码转换成树形结构
        html_tree = etree.HTML(html_data)

        # 使用xpath表达式来筛选书籍的节点标签元素
        book_info_list = html_tree.xpath('//ul[@class="bang_list clearfix bang_list_mode"]/li')

        # 使用循环遍历出每本书的节点信息
        for book_info in book_info_list:
            # 使用xpath表达式来筛选书籍的名称
            book_title = book_info.xpath('./div[@class="name"]/a/@title')[0]
            print(book_title)
            # 使用xpath表达式来筛选书籍的价格
            book_price = book_info.xpath('./div[@class="price"]/p[1]/span[@class="price_n"]/text()')[0]
            print(book_price)

            # 将筛选出的数据打包成列表，并保存到所有书籍信息的列表中
            book_data_list.append([book_title, book_price])

        print(f'==================第{page + 1}页的数据抓取完毕==================')

        # 判断翻页的页数与抓取的页数少一次才执行翻页操作
        if page != pages - 1:
            # 定位翻页按钮，并点击翻页按钮
            driver.find_element(By.XPATH, '//li[@class="next"]/a').click()

        time.sleep(1)

    # 返回所有书籍数据的二维列表
    return book_data_list


def book_info_to_csv(book_info_list):
    # 创建csv文件
    with open('当当图书.csv', 'w', newline='', encoding='utf-8') as file:
        # 使用csv绑定文件对象
        writer = csv.writer(file)

        # 创建表头文件
        writer.writerow(['书籍名称', '书籍价格'])

        # 写入多行数据
        writer.writerows(book_info_list)
    print('数据成功写入到csv文件中')


if __name__ == '__main__':
    # 从键盘输入抓取的页数
    pages = int(input('请输入抓取的页数：'))

    info_list = get_book_info(pages)
    book_info_to_csv(info_list)

    #关闭自动化测试
    options = Options()
    # 添加 experimental_option，禁用自动化扩展，防止被检测到使用了自动化工具进行操作
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 添加 argument，禁用浏览器自动化特性，防止被检测到使用了自动化工具进行操作
    options.add_argument("--disable-blink-features=AutomationControlled")
    # 添加 argument，忽略证书错误，防止因证书错误导致的访问失败
    options.add_argument('ignore-certificate-errors')