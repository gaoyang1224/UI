"""键盘操作"""

from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('http://www.baidu.com')
elem = driver.find_element('id', 'kw')
elem.send_keys('goayang')

# 提交
# 方式一：元素定位
# 方式二：
elem.submit()