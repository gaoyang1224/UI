from selenium import webdriver


def test_start_selenium():
    driver = webdriver.Chrome()
    url = 'http://www.douban.com'
    driver.get(url)

    input_el = driver.find_element('xpath', '//*[@id="anony-nav"]/div[3]/form/span[1]/input')
    input_el.send_keys('老友记')
    input_el.submit()

    # 断言
    actual = driver.title
    # 关闭浏览器
    driver.quit()
    assert actual == '搜索: 老友记'
