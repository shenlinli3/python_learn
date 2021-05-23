# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/19 09:17
@Author  : zero
"""

import hashlib
import random
import string


# 作业：
# 1.实现一个复制函数，参数为两个路径，第一个是源文件的路径，第二个是复制的新文件的路径
def copy(path1, path2):
    with open(path1, "rb") as frb:
        with open(path2, "wb") as fwb:
            fwb.write(frb.read())


# copy("C:/Users/zero/Desktop/test.jpg", "test.jpg")


# 2.实现一个简单的序列化
# students = [
#     {
#         "id": "001",
#         "name": "zhangsan",
#         "age": "18",
#         "sex": "GG",
#         "address": "hangzhou"
#     },
#     {
#         "id": "002",
#         "name": "lisi",
#         "age": "18",
#         "sex": "MM",
#         "address": "hangzhou"
#     },
#     {
#         "id": "003",
#         "name": "wangwu",
#         "age": "3",
#         "sex": "GG",
#         "address": "hangzhou"
#     }
# ]
# with open("students.txt", "w", encoding="utf-8") as fw:
#     for i in students:
#         fw.write(" ".join(i.values()) + "\n")
#
# new_students = []
# stu_keys = ["id", "name", "age", "sex", "address"]
# with open("students.txt", "r", encoding="utf-8") as fr:
#     for stu in fr.read().strip().split("\n"):
#         new_students.append(dict(zip(stu_keys, stu.split())))
# print(students)
# print(new_students)


# 3.实现一个文件hash值对比函数，入参是两个文件的路径
def compare_hash(path1, path2):
    with open(path1, "rb") as frb1:
        with open(path2, "rb") as frb2:
            md5 = hashlib.md5()
            md5.update(frb1.read())
            hash1 = md5.hexdigest()
            md5 = hashlib.md5()
            md5.update(frb2.read())
            hash2 = md5.hexdigest()
            return hash1 == hash2
# print(compare_hash("test.jpg", "C:/Users/zero/Desktop/test.jpg"))


# 4.写出咱们今天写的抽奖程序
# 5.写一个函数随机生成中国大陆手机号 第一位1 第二位3~9 第三到十一位0~9
def rand_tel():
    # tel = "1"
    # tel += str(random.randint(3, 9))
    # for i in range(9):
    #     tel += str(random.randint(0, 9))
    # return tel
    return random.randint(13000000000, 19999999999)
# print(rand_tel())


# 6.写一个函数随机生成四位验证码（验证码包含数字0-9、英文a-zA-Z、都是可能出现、可能重复）
def rand_code(_len=4):
    # upper_letters = [chr(i) for i in range(65, 91)]
    # lower_letters = [i.lower() for i in upper_letters]
    # nums = [str(i) for i in range(10)]
    _code = ""
    for i in range(_len):
        _code += random.choice(string.ascii_letters + string.digits)
    return _code
# print(rand_code(6))