# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/16 09:14
@Author  : zero
"""

# 函数 function method
# 把代码封装起来，便于重复使用，优化代码的逻辑

# 定义一个函数 def
# 函数的命名规则同变量
def my_func_01():
    print("函数内部步骤1")
    print("函数内部步骤2")
    print("函数内部步骤3")

# 执行（调用）一个函数：函数名+括号
# my_func_01()
# my_func_01()
# my_func_01()


### return 返回
# 1.函数中执行到return会马上停止执行并返回
# 2.return会把它后面的值返回给函数的执行者（执行者就是函数名+括号）
# 3.如果return后面没有值，默认返回None
# 4.函数中没有return，那么在函数执行完的时候，也会返回None
def my_func_02():
    print("函数内部步骤1")
    print("函数内部步骤2")
    return  # 函数执行到return的时候会马上停止执行
    print("函数内部步骤3")
    print("函数内部步骤4")
# my_func_02()
# res = my_func_02()
# print(res)

def my_func_03():
    print("函数内部步骤1")
    print("函数内部步骤2")
    return 666 # return会把值（666）返回给函数的执行者
# res = my_func_03()  # 函数的执行者
# print(res)
# print(my_func_03())