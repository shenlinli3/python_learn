# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/16 16:03
@Author  : zero
"""
# 作用域：变量生效的范围

# 内置作用域 B
# 全局作用域 G
# Enclosing E
# 局部作用域 L

# 不同作用域的取值顺序：L -> E -> G -> B
# print(len)
# # len = 10
# def f1():
#     # len = 20  # 相对自己来说是局部，相对inner来说是Enclosing
#     def inner():
#         # len = 30
#         print(len)  # 局部
#     inner()
# f1()


# global
# a = 10
# def test_01():
#     global a  # 声名一个全局变量
#     a += 1  # 在python中的局部作用域，不能修改全局作用域的变量
#     print(a)
# test_01()


# nonlocal
def outer1():
    a = 10
    def inner1():
        nonlocal a  # 把一个局部作用域的变量提升到Enclosing
        a += 1
        print(a)
    inner1()
outer1()

def fc1():
    a = 10
    def fc2():
        nonlocal a
        a += 1  # 11
        print(a)
        def fc3():
            nonlocal a
            a += 1  # 12
            print(a)
        fc3()
    fc2()
    print(a)
fc1()