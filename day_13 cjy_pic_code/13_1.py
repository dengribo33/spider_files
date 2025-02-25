import time
from DrissionPage import ChromiumPage
from PIL import Image, ImageDraw
from chaojiying import Chaojiying_Client

page = ChromiumPage()
page.get('https://passport.fang.com/?backurl=http%3A%2F%2Fmy.fang.com%2F')
time.sleep(2)
# 2、点击账号密码登陆，输入用户名密码，点击登陆按钮
page.ele('xpath=//div[@class="login-cont"]/dt/span[2]').click()
time.sleep(1)
page.ele('@id=username').input('17727274116')
time.sleep(1)
page.ele('@id=password').input('Blzxdrb0508')
time.sleep(1)
#点击登陆按钮
page.ele('@id=loginWithPswd').click()
time.sleep(1)
#点击小滑块
page.ele('xpath=//div[@class="drag-handler verifyicon center-icon"]').click()
time.sleep(2)
# 获取验证码图片
# img_url = driver.find_element(By.XPATH, '//img[@class="img-bg"]').get_attribute('src')
# response = requests.get(img_url)
# with open('code.png', 'wb') as f:
#     f.write(response.content)
img = page('xpath=//img[@class="img-bg"]')
img.save(path='图片', name='验证码.png',rename=False)

# 使用超级鹰识别验证码
cj = Chaojiying_Client('17727274116', '17727274116','964015')
image1 = open('./图片/验证码.png', 'rb').read()
code = cj.PostPic(image1,'9101')['pic_str']
print(code)
x = int(code.split(',')[0])
y = int(code.split(',')[1])
print(x,y)

# 小红点标记
img= Image.open('./图片/验证码.png')
draw = ImageDraw.Draw(img)
box = (x-10, y-10, x+10, y+10)
draw.ellipse(box, fill='red')
img.save('./图片/redcode.png')

#动作链
# actions = webdriver.ActionChains(driver)
#
# slider = driver.find_element(By.XPATH, '//div[@class="drag-handler verifyicon center-icon"]')
#
# actions.click_and_hold(slider)

# # 定位小滑块元素标签
slider = page.ele('xpath=//div[@class="drag-handler verifyicon center-icon"]')

# # 计算出小滑块的宽度
width = slider.rect.size[0]
print('小滑块的宽度为：', width)

x = (x - (width / 2) * 0.9)
print('缩放后的距离：', x)

# 动作链
page.actions.hold(slider).move(x, 0, 1).release()

time.sleep(20)



