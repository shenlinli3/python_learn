# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/12 16:41
@Author  : zero
"""

_list = [3, -7, 8, 1, 5, 2, 1, 10, -5]  # 9个对象
# 每一次比较出一个最大的 n-1  9-1=8次
for i in range(len(_list) - 1):  # 0~7
    for j in range(len(_list) - 1 - i):
        if _list[j] > _list[j + 1]:
            _list[j], _list[j + 1] = _list[j + 1], _list[j]
print(_list)