# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/18 15:31
@Author  : zero
"""

# 一. time 时间模块
# import time
# # 1. time.time()
# print(time.time())  # 从1970-01-01 00:00:00 到现在的秒数（时间戳）
# # 2. time.sleep()  当前线程暂停指定秒数
# time.sleep(1)
# print(time.time())
# # 3. time.strftime()  字符串格式化时间
# print(time.strftime("%Y-%m-%d %H:%M:%S"))


# 二. random 随机模块
# import random
# # 1. random.random()  随机生成0~1的浮点数
# # print(random.random())
# # 2. random.uniform()  !随机生成指定范围的浮点数
# print(random.uniform(3, 5))
# # 3. random.randint()  !随机生成指定范围的整型
# print(random.randint(1, 2))  # 全闭区间
# # 4. random.randrange()  从指定范围的range随机返回一位
# print(random.randrange(1, 11, 2))
# # 5. random.choice()  !从序列中随机抽取一个元素并返回
# print(random.choice([1, 2, 3, 4, 5]))
# # 6. random.sample()  !从序列中随机抽取指定个数的元素并返回
# print(random.sample([1, 2, 3, 4], 2))
# # 7. random.shuffle()  !随机打乱序列
# list01 = [1, 2, 3]
# random.shuffle(list01)
# print(list01)


# 三. hashlib 哈希模块
# 主要是包含了常用的hash算法，哈希算法也叫做散列算法
# import hashlib
# hash_md5 = hashlib.md5("guess_my_pass_!@#$%^&*".encode("utf-8"))
# password = input("请输入密码：")
# hash_md5.update((password + password[::-2]).encode("utf-8"))  # 传入一个字节
# print(hash_md5.hexdigest())  # 查看hash之后的结果
# # 123456 -> md5 hash -> e10adc3949ba59abbe56e057f20f883e  不可还原-不可逆
# # 0b54a35737c187f9d6982125a98d833e
# # 0b54a35737c187f9d6982125a98d833e

# 把程序中的数据或者说抽象的对象存储到文件或者转换可以存储的形式
# 序列化 - 反序列化
students = [
    {
        "id": "001",
        "name": "zhangsan",
        "age": 18,
        "sex": "GG",
        "address": "hangzhou"
    },
    {
        "id": "002",
        "name": "lisi",
        "age": 18,
        "sex": "MM",
        "address": "hangzhou"
    },
    {
        "id": "003",
        "name": "wangwu",
        "age": 3,
        "sex": "GG",
        "address": "hangzhou"
    }
]

