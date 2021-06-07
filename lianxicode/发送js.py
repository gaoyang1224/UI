from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('http://www.baidu.com')

# 执行js指令
js_code = "return doc"
driver.execute_script(js_code)

# 哪些指令在selenium不存在呢
# 改源码
# 滚动条
