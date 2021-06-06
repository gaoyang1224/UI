"""iframe  内嵌网页"""
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("url")

# 想找一个iframe的元素，要进入iframe
# 提供iframe的标识，1.索引，一般不用   2.name属性 = iframeResuit   3.iframe webelement
driver.switch_to.frame(0)               # 索引

driver.switch_to.frame('iframeResuit')  # name 属性

iframe = driver.find_element('xpath', '值')
driver.switch_to.frame(iframe)          # iframe 属性

# 退回主页面
driver.switch_to.default_content()

