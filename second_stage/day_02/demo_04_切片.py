# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/11 11:14
@Author  : zero
"""

# 切片：从序列中切取出一部分
# [start开始:stop结束:step步长]
# 左闭右开  开始包含 结束不包含
# 切片可以倒着取
# 切片越界不会报错

str01 = "hello world!"
print(str01[2:5:1])   # 2包含 5不包含 llo
print(str01[2:7:1])   # 2包含 7不包含 llo w
print(str01[2:7:2])   # low
print(str01[6:-1:1])  # world
print(str01[-5:-1:1])  # orld
print(str01[0:99:1])  # hello world!
print(str01[::])  # hello world! 复制字符串
print(str01[-4:-7:-1])  # 切片的方向和步长要一致 从左到右是正步长 从右到左是负步长
print(str01[::-1])  # 反转字符串

# 现有任意一个字符串如：
# any_str = "   hello world "
# 得到这样一个字符串 "hello world"

any_str = "   hello world "
while any_str[0] == " ":
    any_str = any_str[1:]
while any_str[-1] == " ":
    any_str = any_str[:-1]
print(any_str)
