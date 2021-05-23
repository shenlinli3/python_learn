# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/16 10:44
@Author  : zero
"""

# 函数的参数
# 写一个函数计算圆的面积
def area_of_circle(r):  # 写一个函数，计算圆的面积
    return 3.14 * (r ** 2)

# print(area_of_circle(3))
# print(print("abc"))
# 写一个函数计算可迭代对象的长度
def len_of_iter(iter):
    count = 0
    for i in iter:
        count += 1
    return count
# list01 = [1, 3, 5]
# print(len_of_iter(list01))
# print(len_of_iter("hello"))


# 函数的参数分类
    # 1.形参：函数定义时写在括号中的参数
        # 1.1.位置参数
        # 1.2.默认参数
        # 1.3.动态（可变）位置参数
        # 1.4.动态关键字参数
        # 位置参数 > 动态位置参数 > 默认参数 > 动态关键字参数
    # 2.实参：函数调用时写在括号中的参数
        # 2.1.位置参数
        # 2.2.关键字参数
        # 2.3.混合参数

# def log(a):  # a 在这里就是形参
#     print(a)
# log(10)  # 10 在这里就是实参


# 形参和实参的位置参数
# def f1(num1, num2):
#     print(num1, num2)
# f1(20, 10)  # 参数的个数、位置都要一一对应

# 实参的关键字参数
# def f2(num1, num2):
#     print(num1, num2)
# f2(num2=10, num1=20)

# 实参的混合参数（位置参数+关键字参数）
# def f3(n1, n2, n3):
#     print(n1, n2, n3)
# f3(10, n3=20, n2=30)
# f3(n2=10, 20, 30)  # 报错，关键字参数后面不能有位置参数

# 形参的默认参数
# def my_pow(num1, n=2):  # list.sort()
#     return num1 ** n
# print(my_pow(10, 4))

# 形参的动态位置参数
# def f4(*args):
#     print(args)  # 动态位置参数最终是一个元组
# f4(10, 20, 30, 40)  # 动态位置参数可以接收无数个位置参数

# 形参的动态关键字参数
# def f5(**kwargs):  # keyword
#     print(kwargs)  # 动态关键字参数最终是一个字典
# f5(k1="v1", k2="v2")
# print(dict(k1="v1", k2="v2", k3="v3"))

# 在一个函数中用上所有的形参
# def all_type_arg(a, *args, b=10, **kwargs):
#     print(a, b, args, kwargs)
# all_type_arg(10, 20, 30, 40, 50, b=999, c=666, d=777)

# 形参中的仅限关键字参数
def f6(*args, n):  # 这里的n只能使用实参中的关键字参数给到
    print(args, n)
f6(1, 2, 3, 4, n=5)

def f7(x, y, z, *, n1, n2, n3):
    print(x, y, z)
    print(n1, n2, n3)
f7(666, 777, 888, n1=10, n2=20, n3=30)
