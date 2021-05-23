# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/17 14:12
@Author  : zero
"""

# 闭包：在一个函数中定义了一个内部函数，并且该函数的返回值是这个内部函数（引用），
# 且这个内部函数引用了上级函数的局部（临时）变量，此时这个被引用的变量就叫做自由变量

# def avg_money():
#     _list = []  # 闭包形成的自由变量
#     def inner_func(money):
#         _list.append(money)
#         return sum(_list) / len(_list)
#     return inner_func
#
# company_01_avg = avg_money()
# print(company_01_avg(100000))
# print(company_01_avg(200000))
#
# company_02_avg = avg_money()
# print(company_02_avg(400))
# print(company_02_avg(300))
# print(company_02_avg(300))

def counter():
    exe_count = 0  # 闭包中的自由变量
    def func(s):
        print(f"我是{s}")
        nonlocal exe_count
        exe_count += 1
        print(f"函数被执行了{exe_count}次")
    return func
func01 = counter()
print(func01.__code__.co_freevars)  # 访问一个函数携带的自由变量
func01("f1")
func01("f1")
func01("f1")
func02 = counter()
func02("f2")
func02("f2")
func02("f2")