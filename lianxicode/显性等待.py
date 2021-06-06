from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
url = 'http://www.baidu.com'
driver.get(url)

elem = driver.find_element_by_id('kw')

wait = WebDriverWait(driver, timeout=20)
# 等待元素加载
wait.until(expected_conditions.presence_of_element_located(["id", "kw"]))

# 等待元素可见
wait.until(expected_conditions.visibility_of_element_located(["id", "kw"]))

# 等待元素被点击
wait.until(expected_conditions.element_to_be_clickable(["id", "kw"]))

elem.send_keys('高阳')
elem.submit()

# 显性等待
wait = WebDriverWait(driver, timeout=20)
wait.until(expected_conditions.title_contains('高阳'))

print(driver.title)

driver.close()
