"""alert 弹框"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# 初始化ActionChains:动作链条
action = ActionChains(driver)

# 定位一个元素
elem = driver.find_element('xpath', '//span[text()="设置"]')

# 鼠标悬停 move_to_element
action.move_to_element(elem).perform()

time.sleep(3)

driver.find_element('xpath', '//a[text()="高级搜索"]').click()

# 可以连续操作 （链式调用）
# action.move_to_element(elem).click().drag_and_drop().context_click().perform()

#
# # 单击 click    =elem.click()
# action.click(elem).perform()
#
# # 双击
# action.double_click(elem).perform()
#
# # 右击
# action.context_click(elem).perform()