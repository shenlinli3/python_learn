# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/13 10:19
@Author  : zero
"""

# 字典 dict
# 字典中存储 键值对
# key: value  k: v
# 字典中键具有唯一性，后面出现的会覆盖前面的
# 字典中的键可以是这些数据类型：str（推荐）、num、tuple（不推荐）


# 字典的初始化
# # 1.
# dict01 = {"username": "admin","password": "1234567"}
# print(type(dict01))
# print(dict01)
# # 2.
# dict02 = {}
# print(type(dict02))
# print(dict02)
# # 3.
# dict03 = dict()
# print(type(dict03))
# print(dict03)
# # 4.
# dict04 = dict(username="admin", password="123456")
# print(dict04)
# # 5.
# tuple01 = (("username", "admin"), ("password", "123456"))
# list01 = [["username", "admin"], ["password", "123456"]]
# dict05 = dict(list01)
# print(dict05)
# # 6.
# dict06 = dict(dict05)
# print(dict06)


# # 字典-查
# dict07 = {"username": "admin", "password": "1234567"}
# # 1.使用中括号和键查值
# print(dict07["username"])  # admin
# # print(dict07["username1"])  # 键不存在会报错
# # 2. dict.get()
# print(dict07.get("username"))
# print(dict07.get("username1"))  # 找不到则返回None
# # 3. dict.keys()
# print(list(dict07.keys()))
# # 4. dict.values()
# print(list(dict07.values()))
# # 5. dict.items()
# print(list(dict07.items()))


# # 字典-增
# dict08 = {}
# # 1.
# dict08["username"] = "admin"
# dict08["username"] = "admin1"  # 会覆盖
# print(dict08)
# # 2. dict.setdefault()
# # dict08.setdefault("k3")  # 值可以不填，默认为None
# # dict08.setdefault("k3", "v3")
# dict08.setdefault("username", "admin2")  # 如果键已经存在，值不会覆盖
# print(dict08)
# # 3. dict.update()  # 键已经存在，值会覆盖
# dict08.update({"password": "123456"})  # 合并字典
# print(dict08)
# dict08.update(k1="v1")
# print(dict08)
# dict08.update([["k2", "v2"]])
# print(dict08)


# # 字典-改
# dict09 = {'username': 'admin', 'password': '123456', 'k1': 'v1', 'k2': 'v2'}
# # 1.
# dict09["password"] = '1234567'
# print(dict09)
# # 2. dict.update()
# dict09.update(k1='test')
# print(dict09)


# # 字典-删
# dict09 = {'username': 'admin', 'password': '123456', 'k1': 'v1', 'k2': 'v2'}
# # 1. dict.pop()  删除指定键值对
# print(dict09.pop("username"))
# print(dict09)
# # 2. dict.popitem()  # 字典在python3.6之前是无序的，之前是随机删除，现在删除最后一个
# dict09.popitem()
# print(dict09)
# # 3. del
# del dict09['k1']
# print(dict09)
# # 4. dict.clear()  清空字典
# dict09.clear()
# print(dict09)


# 字典的其它操作
dict10 = {'username': 'admin', 'password': '123456', 'k1': 'v1', 'k2': 'v2'}
# # 1.计算字典的长度
# print(len(dict10))

# # 2.字典的成员运算
# print("k1" in dict10)
# print("k3" not in dict10)

# # 3.字典不能相加！！！ 也不能和整型相乘！！！
# # 4.字典的遍历
for i in dict10.keys():  # 遍历字典的键
    print(i)

for i in dict10:  # 遍历字典，就是遍历字典的键
    print(i)

for i in dict10.values():  # 遍历字典的值
    print(i)

for x, y in dict10.items():  # 遍历字典的键和值
    print(x, y)

