# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/13 15:46
@Author  : zero
"""

# 快速的生成一个列表

# # 列表推导式-循环模式
# # [可加工的变量 for 变量 in 可迭代对象]
# # 1.生成一个1~10的列表
# list01 = [i for i in range(1, 11)]
# print(list01)
# # 2.生成一个1~10的三次方的列表
# list02 = [i ** 3 for i in range(1, 11)]  # 1~10
# print(list02)
# # 3.生成一个列表，包含 user1~user10
# list03 = [("user%d" % i) for i in range(1, 11)]
# print(list03)


# 列表推导式的筛选模式
list04 = [i for i in range(1, 11)]  # 1~10
print(list04)
list05 = [i for i in range(1, 11) if i % 4 != 0]  # 1~10不能被4整除的
print(list05)


# 列表推导式的嵌套模式
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l3 = [j for i in l1 for j in i]
print(l3)
# l2 = []
# for i in l1:
#     for j in i:
#         l2.append(j)
# print(l2)

print("".join(f"{j}x{i}={i * j}\n" if i == j else f"{j}x{i}={i * j}\t" for i in range(1, 10) for j in range(1, i + 1)))