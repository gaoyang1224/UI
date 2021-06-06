import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

url = 'http://www.baidu.com'
driver.get(url)
driver.implicitly_wait(10)

elem = driver.find_element_by_id('kw')
elem.send_keys('高阳')
elem.submit()

all_handlers = driver.window_handles
driver.find_element('xpath', '//span[@class="c-title-text"]').click()

# 切换窗口，传窗口的句柄
# driver.switch_to.window(driver.window_handles[-1])

wait = WebDriverWait(driver, 2)
wait.until(expected_conditions.new_window_is_opened(all_handlers))
# 想打印新页面标题
print(driver.title)
