"""alert 弹框"""

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("url")

h2 =driver.find_element('xpath', '元素')
h2.click()

# 切换到alert,点击确定
alert = driver.switch_to.alert
alert.accept() # 确定
alert.dismiss()  # 取消