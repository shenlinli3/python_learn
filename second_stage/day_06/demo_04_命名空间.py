# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/16 15:23
@Author  : zero
"""

# 内置命名空间
# 全局命名空间
# 局部命名空间

# 加载顺序：内置 > 全局 > 局部
# 取值顺序：局部 > 全局 > 内置

# 验证取值顺序
# print(len)
# # len = 10
#
# def f2():
#     # len = 999
#     print(len)
# f2()


# globals() 返回全局命名空间字典
# locals()  返回局部命名空间字典
num1 = 10
num2 = 20
# print(globals())
# print(locals())  # locals() 在哪一个命名空间被执行，那个命名空间对它而言就是局部
#
# def test_local():
#     n1 = 777
#     n2 = 777
#     print(globals())
#     print(locals())
# test_local()

# 通过globals() 修改全局变量的值
# print(num1)
# globals()['num1'] = 999
# print(num1)
# locals()['num1'] = 666
# print(num1)

# 通过locals() 修改局部变量的值 失败！！！
# def test_01():
#     a = 10
#     b = 20
#     print(a)
#     locals()['a'] = 777  # locals()在局部获取的是一个深拷贝的命名字典
#     print(a)
# test_01()