# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/16 14:07
@Author  : zero
"""

# def f1():
#     print("f1")
#     return "func01"
# def f2():
#     print("f2")
#     return f1()  # func01
# def f3():
#     print("f3")
#     def f1():  # 函数内部可以定义一个函数
#         print("test f1")
#     print(f1())  # 函数内部可以调用一个函数
#     return "func03"


# a, *b, c = 1, 2, 3, 4, 5, 6
# *a, b, c = 1, 2, 3, 4, 5, 6
# a, b, *c = 1, 2, 3, 4, 5, 6
# print(a, b, c)


# def func_01(*args):  # 函数定义时的*有聚合的作用
#     print(args)
# func_01(1, 2, 3 ,4)

# def func_02(n1, n2, n3):
#     print(n1, n2, n3)
# # func_02(1, 2, 3)
# list01 = [1, 2, 3]
# func_02(*list01)  # *在函数调用的时候有打散的作用
# func_02(list01[0], list01[1], list01[2])


# def func_03(**kwargs):  # 聚合
#     print(kwargs)
# func_03(k1="v1", k2="v2")

# def func_04(**kwargs):  # 聚合
#     print(kwargs)
# dict01 = {"k1": "v1", "k2": "v2"}
# func_04(**dict01)  # 打散


# def inner(*args, **kwargs):  # * 聚合
#     print(args, kwargs)
#
# def outer(*args, **kwargs):  # * 聚合
#     print("套娃开始")
#     inner(*args, **kwargs)   # * 打散
#     print("套娃结束")
#
# outer(1, 2, [666, 777], k1="v1", k2="v2")


# def one(s):
#     print(f"我是one {s}")
# def three(**kwargs):
#     print(kwargs)
# def two(*args, **kwargs):
#     print("开始时间：xxxx")
#     three(*args, **kwargs)
#     print("结束时间：xxxx")
#
# two(k1="v1", k2="v2")