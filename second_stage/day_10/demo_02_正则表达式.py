# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/21 15:27
@Author  : zero
"""

# 正则表达式 -> regular expression -> regex -> re

# 元字符
# . 匹配除了换行之外的任意字符
# \d 匹配所有的 数字 0~9
# \D 匹配所有的非 数字
# \w 匹配所有的 英文数字下划线 0~9 a-z A-Z _
# \W 匹配所有的非 英文数字下划线
# \s 匹配所有的 空格、制表、换行
# \S 匹配所有的非 空格、制表、换行
# ^ 限定字符串开头
# $ 限定字符串结尾
# [3456789]  只匹配括号中的内容
# [3-9]  匹配3~9
# [a-zA-Z]  匹配a-z A-Z
# [^a-zA-Z]  匹配所有非 中括号中的内容
# n|m  匹配字符n或者m

# 量词
# {n} 匹配n次
# {n,} 匹配n+次
# {n,m} 匹配n~m次
# ? 0~1次
# + 1~任意次数
# * 0~任意次数

# 怎么取消贪婪匹配呢？
# 在量词后面加上一个?


# re
import re

# # 1.re.match()  match() 会自动给表达式加上开头限定
# tel_pattern = "1[3-9]\d{9}"  # 11位手机号
# res1 = re.match(tel_pattern, "13133931095abc")
# res2 = re.match(tel_pattern, "abc13133931095")
# print(res1, res2, sep="\n")  # 匹配不上，得到的结果是None
#
# # 2.re.search()  没有开头和结尾限定，从任意位置匹配
# tel_pattern = "1[3-9]\d{9}"  # 11位手机号
# res1 = re.search(tel_pattern, "13133931095abc")
# res2 = re.search(tel_pattern, "abc13133931095")
# print(res1, res2, sep="\n")

# # 3.re.findall()  查找所有匹配的子串，并返回一个列表
# tel_pattern = "1[3-9]\d{9}"  # 11位手机号
# str_01 = """u你好18377552232hn378t729u928g63ftb13133931095ub23rhn
# muy33v13133931095ecrv hu344vhwn2343n36tghh513133931095"""
# res = re.findall(tel_pattern, str_01)
# print(res)

sc_pattern = "<dd><a href='(.+?)' >(.+?)</a></dd>"
str_02 = """<dd><a href='/10/10489/4534454.html' >写在连载前</a></dd>
<dd><a href='/10/10489/4535761.html' >第一章 我要减肥！</a></dd>
<dd><a href='/10/10489/9683462.html' >第二章 王宝乐，你干了什么！</a></dd>
<dd><a href='/10/10489/9687224.html' >第三章 好同学，一切有我！</a></dd>
<dd><a href='/10/10489/9687867.html' >第四章 飘渺道院</a></dd>
<dd><a href='/10/10489/9688143.html' >第五章 特招学子</a></dd>
<dd><a href='/10/10489/9690361.html' >第六章 麻烦大了</a></dd>
<dd><a href='/10/10489/9690992.html' >第七章 全民矿工</a></dd>"""
# res = re.findall(sc_pattern, str_02, flags=re.S)  # re.S模式，字符.可以匹配任意（包括换行）
# res = re.findall(sc_pattern, open("../三寸人间.html", "r", encoding='utf-8').read(), flags=re.S)  # re.S模式，字符.可以匹配任意（包括换行）
# print(res)
# for href, name in res:
#     print(href, name)



# 有网址形式为: http://{域名}:端口/share/index.html?参数1={参数1的值}&参数2={参数2的值}
# 如: http://work.dahuatech.com:7076/share/index.html?shareVideold=-721509&playType=1
# 编写程序实现以下功能: 获取分配网址的协议、域名、路径、端口、参数1的值，参数2的值，并以字典的形式打印出结果，
# 如示例中网址的结果为
# {
#     '协议': 'http',
#     '域名': 'work.dahuatech.com',
#     '端口': 7076,
#     '路径': '/share/index.htm/',
#     'shareVideold': '-721509',
#     'playType': 1
# }

url = "http://work.dahuatech.com:7076/share/index.html?shareVideold=-721509&playType=1"
url_pattern = "(.+?)://(.+?)(?::(\d+))?(/.+)?\?"
res = re.search(url_pattern, url)
print(res.groups())  # ('http', 'work.dahuatech.com', '7076', '/share/index.html')
print(res.group(0))  # 匹配的整个规则表达式的子串 http://work.dahuatech.com:7076/share/index.html?
print(res.group(1))  # 第一个括号 http
print(res.group(2))  # 第二个括号 work.dahuatech.com
print(res.group(3))  # 第三个括号 7076
print(res.group(4))  # 第四个括号 /share/index.html
dict_keys = ("协议", "域名", "端口", "路径")
url_dict = dict(zip(dict_keys, res.groups()))
print(url_dict)  # {'协议': 'http', '域名': 'work.dahuatech.com', '端口': '7076', '路径': '/share/index.html'}
url_dict.update(i.split("=") for i in url.split("?")[1].split("&"))
print(url_dict)


num_pattern = "(?:0|[1-9]\d*)(?:\.\d+)?"
str_03 = "ehcvn10dbuen0.1dwugbb999wbb52.6eygn0cec08ecce09cr41rrv0.0jj789456"
res = re.findall(num_pattern, str_03)
print(res)

