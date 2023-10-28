from lxml import etree

# xpath解析
# (1)本地文件  etee.parse

tree = etree.parse('爬虫18_解析_xpath的基本使用.html')
print(tree)

# (2)服务器响应的数据 response.read().decode('utf-8')   *****  etee.HTML()

#tree.xpath('xpath路径')
# #1.路径查询
# # // ->查找所有子孙节点,不考虑层级关系   / ->查找直接子节点
# # 查找ul下面的li
# # li_list = tree.xpath('//body/ul/li')
# li_list = tree.xpath('//body//li')
# print(li_list)
# print(len(li_list))

#2. 谓词查询
#查找所有有id属性的li标签
# text()获取标签中的内容
# li_list = tree.xpath('//ul/li[@id]/text()')
#找到id为l1的标签内容  注意引号的问题
#li_list = tree.xpath("//ul/li[@id = 'l1']/text()")

#3.属性查询
#查找到id为l1的class的属性值
# li_list = tree.xpath("//ul/li[@id='l1']/@class")

#4.模糊查询
#查找id中包含l的li标签
#li_list = tree.xpath("//ul/li[contains(@id,'l')]/text()")
#查找id以l开头的li值
#li_list = tree.xpath("//ul/li[starts-with(@id, 'l')]/text()")

#5.逻辑运算
#查询id为l1和class为c1的标签
#li_list = tree.xpath("//ul/li[@id='l1' and @class='c1']/text()")
li_list = tree.xpath("//ul/li[@id='l1']/text() | //ul/li[@id='l2']/text()")



print(li_list)