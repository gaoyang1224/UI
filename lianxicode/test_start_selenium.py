from selenium import webdriver


def test_start_selenium():
    driver = webdriver.Chrome()
    url = 'http://www.baidu.com'
    driver.get(url)

    # 断言
    assert driver.title == '百度一下，你就知道'
