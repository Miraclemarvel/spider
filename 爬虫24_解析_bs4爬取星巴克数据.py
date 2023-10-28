import urllib.request

url = 'https://www.starbucks.com.cn/menu/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'lxml')

# //ul[@class="grid padded-3 product"]//strong/text()
name_list = soup.select('ul[class="grid padded-3 product"] strong')

# //ul[@class="grid padded-3 product"]//@style
# //ul[@class="grid padded-3 product"]//div[@class='preview circle']
Img_list = soup.find_all("div", class_="preview circle")

import os

i = 0

for Img in Img_list:
    target = Img.get('style').split('"')[1]
    target = "https://www.starbucks.com.cn" + target
    name = name_list[i].get_text()
    name = str(name).replace("/", "or")
    path = './starbucks/' + name + '.jpg'

    urllib.request.urlretrieve(target, path)
    i += 1






# print(Img_list)

