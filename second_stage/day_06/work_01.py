# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/17 09:10
@Author  : zero
"""

'''
作业：温度转换函数，编写程序将用户输入华氏度转换为摄氏度，
或将输入的摄氏度转换为华氏度。
转换算法如下：（C表示摄氏度、F表示华氏度）
     C = ( F - 32 ) / 1.8
     F = C * 1.8 + 32
要求如下：
(1) 输入输出的摄氏度采用大写字母C开头，温度可以是整数或小数，
如：C12.34指摄氏度12.34度；
(2) 输入输出的华氏度采用大写字母F开头，温度可以是整数或小数，
如：F87.65指摄氏度87.65度；
(3) 不考虑异常输入的问题，输出保留小数点后两位；
'''
# def f2c(temp: str):
#     if temp.startswith("C"):
#         return f"F{float(temp[1:]) * 1.8 + 32:.2f}"
#     elif temp.startswith("F"):
#         return f"C{(float(temp[1:]) - 32) / 1.8:.2f}"
# print(f2c("C38.99"))


# 编写一个函数my_sums, 可以接收任意多个数，返回这些数字的和
# def my_sum(*nums):
#     sums = 0
#     for i in nums:
#         sums += i
#     return sums
# print(my_sum(1, 2, 3, 4, 5))


# 编写一个函数cacluate, 可以接收任意多个数，返回的是一个元组，
# 元组的第一个值为所有参数的平均值，第二个值是大于平均值的所有数
# def cacluate(*nums):
#     avg = sum(nums) / len(nums)
#     return avg, [i for i in nums if i > avg]
# print(cacluate(13, 45, 7, 9, 34, 5, 6))


# 写函数，统计字符串中有 几个字母letter，几个数字num，几个空格space，几个其他字符other，
# 并返回类似结果：{'letter': 2, 'num': 3, 'space': 1, 'other': 1}
# def count_char(_str: str):
#     letter = num = space = other = 0
#     for i in _str:
#         if i.isalpha() and i.isascii():
#             letter += 1
#         elif i.isdigit():
#             num += 1
#         elif i == " ":
#             space += 1
#         else:
#             other += 1
#     return {"letter": letter, "num": num, "space": space, "other": other}
# print(count_char("qwer1234    @#$%"))


# 写一个函数，判断用户传入的列表长度是否大于2，如果大于2，只保留前两个，并返回
# def list_len_gt_2(_list: list):
#     return _list[:2] if len(_list) > 2 else _list
# print(list_len_gt_2([1, 2, 3, 4]))
# print(list_len_gt_2([1, 2]))


# 写一个函数，参数是一个字符串，返回值是字符串中大写字母的个数和小写字母的个数
# def case_count(_str: str):
#     upper_case = lower_case = 0
#     for i in _str:
#         if i.isupper():
#             upper_case += 1
#         elif i.islower():
#             lower_case += 1
#     return upper_case, lower_case
# print(case_count("ASDFqwer"))

# 写一个函数，参数是一个字符串，返回值为一个列表，列表中为该字符串各字符在ascii码中的位置
# def index_of_ascii(_str: str):
#     return [ord(i) for i in _str]
# print(index_of_ascii("qwerASDF"))


# 写一个函数，参数是一个字符串，返回值为该字符串去重并排序的结果
# def distinct_and_order(_str: str):
#     str_list = []
#     for i in _str:
#         if i not in str_list:
#             str_list.append(i)
#     str_list.sort()
#     return "".join(str_list)

def distinct_and_order(_str: str):
    # _list = list(set(_str))
    # _list.sort()
    # return "".join(_list)
    return "".join(sorted(set(_str)))

print(distinct_and_order("abcDDCDCD"))