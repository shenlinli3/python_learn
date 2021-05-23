# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/14 11:37
@Author  : zero
"""

# Python基础数据类型-六种
# 1.数字 num
    # 1.1.整型 int
    # 1.2.浮点型 float
    # 1.3.复数 complex
    # 1.4.布尔 bool
        # 1.4.1 真 True
        # 1.4.2 假 False
# 2.字符串 str
# 3.列表 list
# 4.元组 tuple
# 5.字典 dict
# 6.集合 set
# 7.空 None


# 三种不可变
    # 数字 num
    # 字符串 str
    # 元组 tuple
# 三种可变
    # 列表 list
    # 字典 dict
    # 集合 set


# 基础数据类型的 成员运算
# 除了数字型num，都可以使用成员运算
# print(1 in 123)  # 报错
print("a" in "abc")  # True
print("a" in ["abc", "b"])  # False
print("a" in ("abc", "bbc"))  # False
print("a" in {"a": "b"})  # True
print("a" in {"abc", "a"})  # True


# 序列的长度运算，除了数字型num，都可以使用len()
# print(len(123))  # 报错 TypeError: object of type 'int' has no len()
print(len("abc"))  # 3
print(len([1, 2, 3, "a", True]))  # 5
print(len((1, 2, 3, "a", True)))  # 5
print(len({"k1": "v1", "k2": "v2"}))  # 2
print(len({1, 2, 3, "a", True}))  # 4



# # # 可迭代对象之间的转换

# # str -> list
# print(list("hello"))
# # str -> tuple
# print(tuple("hello"))
# # str -> set
# print(set("hello"))

# # list -> str
# print("".join(["a1", "b2", "3"]))
# # list -> tuple
# print(tuple([1, 2, 3]))
# # list -> set
# print(set([1, 2, 3, 3]))

# # tuple -> str
# print("".join(("abc", "b")))
# # tuple -> list
# print(list((1, 2, 3)))
# # tuple -> set
# print(set((1, 2, 3)))

# # set -> str
# print("".join({"abc", "ert"}))
# # set -> list
# print(list({1, 2, 3}))
# # set -> tuple
# print(tuple({1, 2, 3}))

# # list -> dict
# print(dict([["k1", "v1"], ["k2", "v2"], ["k3", "v3"]]))
# # tuple -> dict
# print(dict((("k1", "v1"), ("k2", "v2"), ["k3", "v3"])))
# # set -> dict
# print(dict({("k1", "v1"), ("k2", "v2")}))