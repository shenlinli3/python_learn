# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/21 10:21
@Author  : zero
"""

# 求1~10所有数的和
# sums = 0
# for i in range(1, 11):
#     sums += i
# print(sums)


# 使用递归完成求和 可能会造成栈溢出
def sums(n):
    if n == 1:
        return 1
    else:
        return n + sums(n - 1)


print(sums(3))


# return 3 + sums(2)
# return 2 + sums(1)
# sums(1) -> 1