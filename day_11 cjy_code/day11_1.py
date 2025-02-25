from selenium import webdriver
from chaojiying import Chaojiying_Client
import time
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get('https://www.chaojiying.com/user/login/')
#定位
img = driver.find_element(By.XPATH, '//form[@name="fm2"]/div/img')
# 截图
img.screenshot('验证码.png')
# 实例化
chaojiying = Chaojiying_Client('17727274116', '17727274116','964015')
# 打开并读取验证码图片
image = open('../day_18 socket/server/验证码.png', 'rb').read()
# 识别验证码
code = chaojiying.PostPic(image, 1902)['pic_str']

# 输入用户名
driver.find_element(By.NAME, 'user').send_keys('17727274116')
time.sleep(2)
# 输入密码
driver.find_element(By.NAME, 'pass').send_keys('17727274116')
time.sleep(2)
# 输入验证码
driver.find_element(By.NAME, 'imgtxt').send_keys(code)
time.sleep(2)
# 点击登录
driver.find_element(By.XPATH, '//input[@type="submit"]').click()

time.sleep(10)





