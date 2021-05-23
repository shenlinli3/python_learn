# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/14 14:23
@Author  : zero
"""

# 非0即True
# 非空即True
# 非None即True


# # 数字型 -> 布尔
# # num -> bool
# print(bool(1))  # True
# print(bool(0))  # False
# print(bool(2))  # True
# print(bool(-2))  # True
# print(bool(9.9))  # True
# print(bool(0.0))  # False

# # 字符串 -> 布尔
# # str -> bool
# print(bool("hello"))  # True
# print(bool(" "))  # True
# print(bool(""))  # True

# # 列表 -> 布尔
# # list -> bool
# print(bool([1, 2, 3]))  # True
# print(bool([]))  # False

# # 元组 -> 布尔
# # tuple -> bool
# print(bool((1, 2, 3)))  # True
# print(bool(tuple()))  # False

# # 集合 -> 布尔
# # set -> bool
# print(bool({1, 2, 3}))  # True
# print(bool(set()))  # False

# # 字典 -> 布尔
# # dict -> bool
# print(bool({"k1": "v1"}))  # True
# print(bool({}))  # False

# # 空 -> 布尔
# # None -> bool
# print(bool(None))  # False


# ### 判断列表是否为空
# 1.
# _list = [1]
# if len(_list) != 0:
#     print("有")
# else:
#     print("无")

# # 2.
# _list = [1]
# if bool(_list):
#     print("有")
# else:
#     print("无")

# 3.
_list = []
# if _list:
#     print("有")
# else:
#     print("无")
print("有" if _list else "无")