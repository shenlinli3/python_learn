# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/17 11:20
@Author  : zero
"""

# map()  遍历
# 两个参数：函数、可迭代对象
# list01 = [1, -2, 3, -4, 5]
# def pow2(num):
#     return num ** 2
# print(list(map(pow2, list01)))
# print(list(map(lambda x: x ** 2, list01)))
# print(list(map(abs, list01)))


# filter()  过滤器
# list02 = [1, -2, 3, -4, 5]
# def positive_number_filter(x):
#     return x > 0  # True
# print(list(filter(positive_number_filter, list02)))
# print(list(filter(lambda x: x > 0, list02)))


# reduce()
# from functools import reduce  # 从functools模块导入reduce函数
# list03 = [1, 2, 3, 4, 5]
# def r(num1, num2):
#     return num1 * 10 + num2
# print(reduce(r, list03))
# print(reduce(lambda num1, num2: num1 * 10 + num2, list03))


# sorted() 排序，不改变序列本身，返回值是一个新列表
# list04 = [1, -2, 3, -4, 5]
# print(sorted(list04))
# print(sorted(list04, reverse=True))
# print(sorted(list04, key=abs))
# print(list04)

students = [
    {'name': '张三', 'age': 23, 'score': 88, 'tel': '23423532', 'gender': '男'},
    {'name': '李四', 'age': 26, 'score': 80, 'tel': '12533453', 'gender': '女'},
    {'name': '王五', 'age': 15, 'score': 58, 'tel': '56453453', 'gender': '男'},
    {'name': '赵六', 'age': 16, 'score': 57, 'tel': '86786785', 'gender': '不明'},
    {'name': '小明', 'age': 18, 'score': 98, 'tel': '23434656', 'gender': '女'},
    {'name': '小红', 'age': 23, 'score': 72, 'tel': '67867868', 'gender': '女'},
]

print(sorted(students, key=lambda x: x["age"]))
print(sorted(students, key=lambda x: x["score"]))

# 有这样一个字符串 "12345"，不可以使用int()，使用reduce把它转换为12345整型