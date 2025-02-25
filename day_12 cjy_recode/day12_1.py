import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image, ImageDraw
from selenium.webdriver.edge.options import Options
from chaojiying import Chaojiying_Client

# 1、关闭自动化
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument('--disable-blink-features=AutomationControlled')
# 关闭证书报错
options.add_argument('ignore-certificate-errors')

driver = webdriver.Edge(options=options)
driver.get('https://passport.fang.com/?backurl=http%3A%2F%2Fmy.fang.com%2F')
time.sleep(2)
# 2、点击账号密码登陆，输入用户名密码，点击登陆按钮
driver.find_element(By.XPATH, '//div[@class="login-cont"]/dt/span[2]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('17727274116')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Blzxdrb0508')
time.sleep(1)
#点击登陆按钮
driver.find_element(By.XPATH, '//button[@id="loginWithPswd"]').click()
time.sleep(1)
#点击小滑块
driver.find_element(By.XPATH, '//div[@class="drag-handler verifyicon center-icon"]').click()
time.sleep(2)
# 获取验证码图片
img_url = driver.find_element(By.XPATH, '//img[@class="img-bg"]').get_attribute('src')
response = requests.get(img_url)
with open('code.png', 'wb') as f:
    f.write(response.content)

# 使用超级鹰识别验证码
cj = Chaojiying_Client('17727274116', '17727274116','964015')
image1 = open('code.png', 'rb').read()
code = cj.PostPic(image1,9101)['pic_str']
print(code)
x = int(code.split(',')[0])
y = int(code.split(',')[1])
print(x,y)

# 小红点标记
img= Image.open('code.png')
draw = ImageDraw.Draw(img)
box = (x-10, y-10, x+10, y+10)
draw.ellipse(box, fill='red')
img.save('redcode.png')

#动作链
actions = webdriver.ActionChains(driver)

slider = driver.find_element(By.XPATH, '//div[@class="drag-handler verifyicon center-icon"]')

actions.click_and_hold(slider)

#计算滑动距离
width = slider.size['width']
print("width:",width)

end_x = int(x-(width/2)*1.05)
print("end_x:",end_x)

actions.move_by_offset(end_x, 0).release().perform()

time.sleep(30)



