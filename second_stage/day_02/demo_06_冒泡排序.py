# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/11 17:06
@Author  : zero
"""

# 冒泡排序：每一轮排出一个最大的放在最后面
# 如果列表有n个数字，则总共进行n-1轮
_list = [3, -7, 8, 1, 5, 2, 1, 10, -5]
outer_index = 0
while outer_index < len(_list) - 1:  # 0 1 2
    inner_index = 0
    while inner_index < len(_list) - 1 - outer_index:  # 0 ~ 3
        if _list[inner_index] < _list[inner_index + 1]:
            temp = _list[inner_index]
            _list[inner_index] = _list[inner_index + 1]
            _list[inner_index + 1] = temp
        inner_index += 1
    outer_index += 1
print(_list)