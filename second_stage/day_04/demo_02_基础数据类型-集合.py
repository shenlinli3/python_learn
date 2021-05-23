# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/13 15:14
@Author  : zero
"""

# 集合 set
# 集合是无序的
# 集合中的对象具有唯一性

# 集合的初始化
# 1.
set01 = {1, 2, 3, 4}
print(type(set01))
print(set01)
# 2.
# set02 = set("hello")  # str\list\tuple
# set02 = set([1, 2, 3, 3, 4, 2])  # str\list\tuple
set02 = set((1, 2, 3, 3, 4, 2))  # str\list\tuple
print(type(set02))
print(set02)


# 集合的操作
set03 = {1, 2, 3, 4}
set04 = {3, 4, 5, 6, 7}
# 交集
print(set03 & set04)  # {3, 4}
# 并集
print(set03 | set04)  # {1, 2, 3, 4, 5, 6, 7}
# 差集
print(set03 - set04)  # {1, 2}
print(set04 - set03)  # {5, 6, 7}
# 并集 - 交集 = 对称差集
print(set03 ^ set04)  # {1, 2, 5, 6, 7}
# 集合添加一个对象
set03.add(666)
set03.remove(4)
print(set03)

# 计算长度
print(len({1, 2, 3}))  # 3
# 成员运算
print(1 in {1, 2, 3})  # True

# 列表、字符串、元组 去重
list01 = [1, 2, 2, 3, 4, 4]
list01 = list(set(list01))
print(list01)