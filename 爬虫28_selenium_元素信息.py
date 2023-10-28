from selenium import webdriver

path = 'msedgedriver.exe'

browser = webdriver.Edge(path)

url = 'https://www.baidu.com'

browser.get(url)

# 获取标签属性
input = browser.find_element_by_id('su')
print(input.get_attribute('class'))

# 获取标签名
print(input.tag_name)

# 获取元素文本
a = browser.find_element_by_link_text('新闻')
print(a.text)