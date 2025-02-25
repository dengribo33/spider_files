import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options


# options = Options()
#
# options.add_argument('--headless')
#
# driver = webdriver.Edge(options=options)

driver = webdriver.Edge()

driver.get('https://www.baidu.com')

input_element = driver.find_element(By.ID, 'kw')
input_element.send_keys('美女')

button_element = driver.find_element(By.ID, 'su')
button_element.click()


time.sleep(5)
beauty_women = driver.page_source

with open('beauty_women.html', 'w', encoding='utf-8') as f:
    f.write(beauty_women)

driver.quit()











