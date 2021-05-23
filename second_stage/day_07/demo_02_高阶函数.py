# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/17 10:20
@Author  : zero
"""

# 什么是高阶函数
# 答：就是可以把函数作为参数传递的函数

# 列表根据数字的绝对值排序
# _list = [1, 3, 2, -4, 5, 3, -2, 7]
# # [1, 3, 2, 4, 5, 3, 2, 7]
# _list.sort(key=abs)  # 这里的key接收一个函数
# print(_list)

# 列表根据字符串的长度排序
# _list = ["abcd", "fgh", "1234ed", "77777", "z"]
# _list.sort(key=len)  # 4 3 6 5 1
# print(_list)


# # 我想设计一个求和函数，入参是两个数字，出参是它们绝对值的和
# def abs_add(num1, num2):
#     return abs(num1) + abs(num2)
# print(abs_add(10, -10))
# # 我还想设计一个求和函数，入参是两个数字，出参是它们三次方的和
# def pow3_add(num1, num2):
#     return num1 ** 3 + num2 ** 3
# print(pow3_add(10, -9))
# # 把上面两个函数结合起来
# def diy_add(num1, num2, func):
#     return func(num1) + func(num2)
# print(diy_add(10, -10, abs))
# print(diy_add(10, -9, lambda x: x ** 3))

# nums = [3, -4, 2, 7, 1, 0, -5, 9]
# nums.sort()
# print(nums)

students = [
    {'name': '张三', 'age': 23, 'score': 88, 'tel': '23423532', 'gender': '男'},
    {'name': '李四', 'age': 26, 'score': 80, 'tel': '12533453', 'gender': '女'},
    {'name': '王五', 'age': 15, 'score': 58, 'tel': '56453453', 'gender': '男'},
    {'name': '赵六', 'age': 16, 'score': 57, 'tel': '86786785', 'gender': '不明'},
    {'name': '小明', 'age': 18, 'score': 98, 'tel': '23434656', 'gender': '女'},
    {'name': '小红', 'age': 23, 'score': 72, 'tel': '67867868', 'gender': '女'},
]


def get_score(_dict):
    return _dict["score"]


# 将列表按学生成绩从大到小排序
students.sort(key=get_score, reverse=True)
students.sort(key=lambda x: x["score"], reverse=True)
students.sort(key=lambda x: x["age"], reverse=True)
print(students)
