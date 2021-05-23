# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/13 16:39
@Author  : zero
"""

# 字符串是可以比较大小的
s1 = "abcd"
s2 = "bbbb"
s3 = "bbb"
s4 = "cde"
s5 = "abb"
s6 = "ABCD"

print(s1 > s2)  # False
print(s1 > s6)  # True
print(s1 > s5)  # True
# 按照在ascii码中的顺序，在ascii码中位置越靠后越大
# 先比较第一个，如果相同则依次比较后续的