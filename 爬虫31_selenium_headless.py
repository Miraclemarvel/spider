# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.edge.options import Options
#
# #edge_options = Options()
# EDGE = {
#     "browserName": "MicrosoftEdge",
#     "version": "92.0.902.55",
#     "platform": "WINDOWS",
#     "ms:edgeOptions": {
#         'extensions': [],
#         'args': [
#             '--headless',
#             '--disable-gpu'
#         ]}
# }
# bro = webdriver.Edge('msedgedriver.exe',capabilities=EDGE)
# #浏览器无可视化界面
# url = 'https://www.baidu.com'
# bro.get(url)
#
# bro.save_screenshot('baidu1.png')

# 封装的headless

from selenium import webdriver
from selenium.webdriver.edge.options import Options

def share_browser():
    #edge_options = Options()
    EDGE = {
        "browserName": "MicrosoftEdge",
        "version": "92.0.902.55",
        "platform": "WINDOWS",
        "ms:edgeOptions": {
            'extensions': [],
            'args': [
                '--headless',
                '--disable-gpu'
            ]}
    }
    browser = webdriver.Edge('msedgedriver.exe',capabilities=EDGE)
    return browser
#
# browser = share_browser()
# url = 'https://www.baidu.com'
#
# browser.get(url)