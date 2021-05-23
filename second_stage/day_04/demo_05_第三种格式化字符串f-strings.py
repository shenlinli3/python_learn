# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/13 16:27
@Author  : zero
"""

# Python3.6+版本 添加了f-strings
name01 = "zhangsan"
name02 = "lisi"
hobby01 = "python"
hobby02 = "java"
print("%s like %s\n%s like %s" % (name01, hobby01, name02, hobby02))
print("{} like {}\n{} like {}".format(name01, hobby01, name02, hobby02))
print(f"{name01} like {hobby01}\n{name02} like {hobby02}")

print([f"user{i}" for i in range(1, 11)])