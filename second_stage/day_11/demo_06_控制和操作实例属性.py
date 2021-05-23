# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/22 16:37
@Author  : zero
"""
# 函数dir() 查看一个对象所有的属性

# __slots__
class Person:
    __slots__ = ("name", "age", "sex")  # 限制对象能够绑定的属性
    pass

p1 = Person()
p1.name = "zhansgan"
p1.age = 17
p1.sex = "GG"
# p1.girl_friend = "xiaohong"
print(dir(p1))


# hasattr()  判断指定对象是否有指定属性
print(hasattr(p1, "name"))  # True
print(hasattr(p1, "girl_friend"))  # False
# getattr()  获取指定对象的指定属性
print(getattr(p1, "name"))
print(getattr(p1, "girl_friend", None))
# setattr()  设置指定对象的指定属性
setattr(p1, "name", "lisi")
print(p1.name)
