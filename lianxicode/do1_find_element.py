from selenium import webdriver
driver = webdriver.Chrome()
url = 'http://www.douban.com'
driver.get(url)

ele = driver.find_element_by_name('q')
print(ele)

# 打印标签名
print(ele.tag_name)

# 属性和方法
print(ele.send_keys('你好呀'))

# 获取元素的属性
print(ele.get_attribute('maxlength'))


# find_element和find_elements的区别
ele = driver.find_elements_by_name('q')
print(ele)
"""find_element得到的是一个WebElement的对象
find_elements得到的是一个列表"""
"""
try:
    driver.find_element_by_name('q')
    print("元素存在")
except:
    print("元素不存在")   
"""

driver.close()