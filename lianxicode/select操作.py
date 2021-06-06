"""select"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("url")

# 直接定位元素，点击
driver.find_element('xpath', "//option[text()='yuz']").click()


