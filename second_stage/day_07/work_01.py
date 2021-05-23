# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/18 09:15
@Author  : zero
"""
# 现有任意一个列表 [-1, -5, 2, 4, 6, -2, 0, 9]，完成如下需求：小于0的全部放到列表的右边，
# 大于等于0的全部放到列表的左边，小于0的部分按照从大到小排序，大于等于0的部分按照从小到大排序

# _list = [-1, -5, 2, 4, 6, -2, 0, 9]
# _list = sorted(filter(lambda x: x >= 0, _list), reverse=True) \
#         + sorted(filter(lambda x: x < 0, _list), reverse=False)
# # _list = sorted(filter(lambda x: x < 0, _list), reverse=False) \
# #         + sorted(filter(lambda x: x >= 0, _list), reverse=False)
# print(_list)


# 小于0的全部放到列表的右边，大于等于0的全部放到列表的左边，小于0的部分按照从大到小排序，大于等于0的部分按照从小到大排序
# _list = [-1, -5, 2, 4, 6, -2, 0, 9]
# print(sorted(_list, key=lambda x: (x < 0, abs(x))))
# for i in _list:
#     print((lambda x: (x < 0, x))(i))