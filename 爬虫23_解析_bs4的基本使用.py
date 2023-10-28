from bs4 import BeautifulSoup

# 通过解析本地文件 来将bs4的基础语法进行讲解
#默认打开文件的编码格式为gbk编码
soup = BeautifulSoup(open("爬虫23_解析_bs4的基本使用.html",encoding='utf-8'), 'lxml')

# #根据标签名字查询节点
# #找到的是第一个符合条件的数据
# print(soup.a)
# #attrs用来获取标签的属性和属性值
# print(soup.a.attrs)

#bs4的一些函数
# (1)find
#返回的是第一个符合条件的数据
# print(soup.find('a'))
#根据title的值来找到对应的标签对象
# print(soup.find('a',title = 'a2'))
#根据class的属性找到对应的标签对象,注意class要加下划线
#print(soup.find('a', class_ = 'a1'))

# (2)find_all 返回的是一个列表 并且返回了所有的a标签
# print(soup.find_all('a'))
# 如果想获取多个标签的数据 那么需要在find_all的参数中添加的是列表的数据
# print(soup.find_all(['a','span']))
#limit的作用是查找前几个数据
# print(soup.find_all('li', limit = 2))

# (3)select(推荐)
#select方法返回的是一个列表, 并且会返回多个数据
# print(soup.select('a'))
# 可以通过.代表class  我们把这种操作称为类选择器
#print(soup.select('.a1'))
#print(soup.select('#l1'))
#属性选择器
#查找到li标签中有id的标签
# print(soup.select('li[id]'))
#查找到li标签中为l2的标签
# print(soup.select('li[id="l2"]'))
#层级选择器
#后代选择器
#找到div的li
# print(soup.select(('div li')))
#子代选择器
#某标签的第一级子标签
#注意: 很多的计算机编程语言中 如果不加空格不会输出内容 但是在bs4中 不会报错 会显示内容
# print(soup.select("div>ul>li"))
#找到a和li标签的所有对象
# print(soup.select('a, li'))

#节点信息
#获取节点内容
# obj = soup.select('#d1')[0]
#如果标签中只有内容 那么string和get_text()都可以使用
#如果标签对象中 除了内容还有标签 那么string就获取不到数据 而get_text()可以获取数据
#我们一般情况下推荐使用get_text()
# print(obj.get_text())
#节点的属性
# obj = soup.select('#p1')[0]
# print(obj.name)
#将属性值作为一个字典返回
# print(obj.attrs)

#获取节点的属性
# obj = soup.select("#p1")[0]
# print(obj.attrs.get('class'))
# print(obj.get('class'))
# print(obj['class'])