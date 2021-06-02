import time

from selenium import webdriver

driver = webdriver.Chrome()

# 隐形等待,只要设置一次，只能等待元素
driver.implicitly_wait(10)

driver.get('http://www.baidu.com')

elen = driver.find_element_by_id('kw')
elen.send_keys("陕西")
elen.submit()

# 等待
time.sleep(3)

print(driver.title)
print(driver.current_url)
# print(driver.page_source)

# 刷新
driver.refresh()

# 访问一个另外的网址
driver.get("http://www.baidu.com")

# 回退
driver.back()

# 前进
driver.forward()

# 最小化窗口
driver.maximize_window()

# 最大化窗口
driver.minimize_window()

# 全屏
driver.fullscreen_window()

# 固定尺寸窗口
driver.set_window_size(400, 300)

# 关闭浏览器
driver.quit()

# 关闭标签页
driver.close()
