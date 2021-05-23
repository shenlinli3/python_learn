# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/14 16:35
@Author  : zero
"""

# copy 拷贝、复制

# # 浅拷贝
# list01 = [1, 2, 3, 4, [666, 777]]
# list02 = list01.copy()
# print(list01)
# print(list02)
# list01[0] = 678
# print(list01)
# print(list02)
# list01[4][0] = 999
# print(list01)
# print(list02)


# 深拷贝
import copy  # 导入一个叫做copy的模块
list01 = [1, 2, 3, 4, [666, 777]]
list02 = copy.deepcopy(list01)  # 深复制
print(list01)
print(list02)
list01[0] = 678
print(list01)
print(list02)
list01[4][0] = 999
print(list01)
print(list02)