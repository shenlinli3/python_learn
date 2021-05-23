# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/12 15:27
@Author  : zero
"""

# 元组 tuple
# 元组和列表非常的相似，区别就是元组使用()括号，另外元组不可变

# # 元组的初始化
# # 1.
# tuple01 = (1, 2, 3)
# print(type(tuple01))
# print(tuple01)
# # 2.
# # tuple02 = ()
# tuple02 = (1, )  # 当元组中只有一个对象的时候，在该对象后面加上一个逗号
# print(type(tuple02))
# print(tuple02)
# # 3.
# # tuple03 = tuple()
# # tuple03 = tuple("hello")
# tuple03 = tuple([1, 2, 3, 4])
# print(tuple03)


# # 元组-查
# tuple04 = (1, 2, 3, True, "abc", [666, 777])
# # 1.索引
# print(tuple04[3])
# # 2.切片
# print(tuple04[3:5])
# # 3. tuple.index()
# print(tuple04.index("abc"))
# # 4. tuple.count()
# print(tuple04.count(1))


# 元组不可变
# tuple04[0] = 789  # 会报错


# # 元组的其它操作
# # 1.成员运算
# print(1 in (1, 2, 3))
# # 2.计算长度
# print(len((1, 2, 3)))
# # 3.元组和元组相加
# print((1, 2) + (3, 4))
# # 4.元组和整型相乘
# print((1, 2, 3) * 2)


# # 元组的自动打包和拆包
# t1 = (1, 2, 3)
# print(t1)
# # 在python中，把多个值赋给一个变量的时候，会自动把这些值打包成一个元组
# t2 = 1, 2, 3
# print(t2)
#
# t3 = (1, 2, 3)
# a, b, c = t3  # 自动解包
# print(a, b, c)

# 变量交换
num1 = 10
num2 = 20
# 1.
# temp = num1
# num1 = num2
# num2 = temp
# print(num1, num2)
# 2.
# num1 = num1 + num2  # 30
# num2 = num1 - num2  # 10
# num1 = num1 - num2  # 20
# print(num1, num2)
# 3.
num1, num2 = num2, num1
print(num1, num2)