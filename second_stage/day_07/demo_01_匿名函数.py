# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/17 10:04
@Author  : zero
"""

# 函数名就相当于一个变量，函数也可以赋给多个变量
# def f1():
#     print("我是f1")
# f2 = f1
# print(f1)
# print(f2)
# f1()
# f2()

# lambda 函数
def pow3(num):
    return num ** 3
print(pow3(3))

lambda_pow3 = lambda num: num ** 3
print(lambda_pow3(3))

lambda_add = lambda num1, num2: num1 + num2
print(lambda_add(10, 91))

print((lambda num1, num2: num1 * num2)(10, 91))