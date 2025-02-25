import time
import requests
from selenium import webdriver
from PIL import Image, ImageDraw
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

# 1、因为房天下网站登陆会检测自动化程序，所以需要关闭selenium的自动化特性，防止被检测到
options = Options()
# 设置自动化特性扩展的关闭，防止被服务器检测到是由selenium驱动的
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 设置关闭自动化特性，防止被服务器检测到是由selenium驱动的
# 这里之前第11节课里的值些错了，大家记得改一下，AutomationsControlled多了一个s
options.add_argument('--disable-blink-features=AutomationControlled')
# 关闭证书报错
options.add_argument('ignore-certificate-errors')
# 2、实例化谷歌浏览器对象,打开对应的网页并设置窗口最大化
driver = webdriver.Edge(options=options)
driver.get('https://passport.fang.com/?backurl=https%3A%2F%2Fcs.fang.com%2F')
driver.maximize_window()
time.sleep(1)
# 3、定位账号密码登录的标签，并点击该标签切换登录的方式
driver.find_element(By.XPATH, '//div[@class="login-cont"]/dt/span[2]').click()
time.sleep(1)
# 4、定位账号输入框的标签，并输入登录的账号
driver.find_element(By.XPATH,
'//input[@id="username"]').send_keys('xinyu_teacher')
time.sleep(1)
# 5、定位密码输入框的标签，并输入账号的密码
driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('Xin6Yu6T')
time.sleep(1)
# 6、定位登录的按钮标签，并点击登录按钮
driver.find_element(By.XPATH, '//button[@id="loginWithPswd"]').click()
time.sleep(1)
# 7、定位小滑块的元素标签，并点击这个小滑块
driver.find_element(By.XPATH, '//div[@class="drag-handler verifyicon centericon"]').click()
time.sleep(3)