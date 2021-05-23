# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/12 16:06
@Author  : zero
"""

# for循环

"""
for 变量名 in 可迭代对象:
    print(变量名)
    ...
"""

# 遍历字符串
# str01 = "hello world!"  # 12
# for i in str01:
#     print(i)

# 遍历列表
# list01 = [1, 2, 3, 4, 5]
# for j in list01:
#     print(j)

# 遍历元组
# tuple01 = (1, 2, 3, 4, 5)
# for x in tuple01:
#     print(x)


# # 函数 range() 返回指定范围的生成器、懒序列
# # start, stop, step  左闭右开
# print(list(range(1, 11, 1)))
# print(list(range(1, 11, 2)))
# print(list(range(1, 11, 3)))
# # 如果只有一个参数，那么这个参数被认为是stop，start默认为0
# print(list(range(100)))  # range(0, 100)

# 10000次循环
# for i in range(10000):
#     print(i)

# 1~100求和
# sums = 0
# for i in range(1, 101):
#     sums += i
# print(sums)

# for循环中的break、continue
for i in range(1, 101):
    if i == 77:
        break
    print(i)

for i in range(1, 101):
    if i == 77:
        continue
    print(i)