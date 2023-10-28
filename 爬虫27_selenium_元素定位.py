from selenium import webdriver

path = 'msedgedriver.exe'

browser = webdriver.Edge(path)

url = 'https://www.baidu.com'

browser.get(url)

# 元素定位
# 1. 根据id找到对象                                             *****
# button = browser.find_element_by_id('su')
# print(button)

# 2. 根据标签属性的属性值来获取对象
# button = browser.find_element_by_name('wd')
# print(button)

# 3.根据xpath语句来获取对象 (elements返回列表, element返回对象)      *****
# button = browser.find_element_by_xpath('//input[@id="su"]')
# print(button)

# 4. 根据标签的名字来获取对象 (elements返回列表, element返回对象)
# button = browser.find_elements_by_tag_name('input')
# print(button)

# 5. 使用bs4的语法来获取对象                                      *****
# button = browser.find_element_by_css_selector('#su')
# print(button)

# 6. 根据链接按钮获取对象
# button = browser.find_elements_by_link_text('贴吧')
# print(button)