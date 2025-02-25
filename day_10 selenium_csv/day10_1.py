from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import csv
from selenium.webdriver.edge.options import Options

def get_page_info(pages):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Edge(options=options)
    # driver = webdriver.Edge()
    driver.get("http://bang.dangdang.com/books/bestsellers/01.03.00.00.00.00-24hours-0-0-1-1")

    book_data_list = []

    for page in range(pages):
        # 滚蛋等待页面加载完成
        for i in range(1,4):
            # 随机等待时间
            random_time = random.randint(1, 3)
            time.sleep(random_time)
            # 随机滚动屏幕
            random_y = random.randint(500, 1000)
            driver.execute_script(f"window.scrollTo(0, {i*random_y});")

        # 解析页面数据
        html_data = driver.page_source
        html_tree = etree.HTML(html_data)

        # 筛选出书籍列表
        book_info_list = html_tree.xpath('//ul[@class="bang_list clearfix bang_list_mode"]/li')

        # 遍历书籍列表，获取书籍信息
        for book_info in book_info_list:
            book_name = book_info.xpath('./div[@class="name"]/a/@title')[0]
            book_author = book_info.xpath('./div[@class="publisher_info"][1]/a[1]/text()')[0]
            book_price = book_info.xpath('./div[@class="price"][1]/p[1]/span[1]/text()')[0]
            book_time = book_info.xpath('./div[@class="publisher_info"]/span/text()')[0]

            book_data_list.append([book_name, book_author, book_price, book_time])

        print(f"the {page+1} save")


        # 点击下一页
        if page != pages - 1:
            driver.find_element(By.XPATH, '//li[@class="next"]/a').click()

        time.sleep(2)

    return book_data_list

def save_data_csv(x):
    with open('book-data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        writer.writerow(['书名', '作者', '价格', '出版时间'])

        writer.writerows(x)
    print('数据保存成功！')

if __name__ == '__main__':
    pages = int(input("请输入要爬取的页数："))

    info_list = get_page_info(pages)
    save_data_csv(info_list)


