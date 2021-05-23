# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/22 11:41
@Author  : zero
"""


# 面向对象的三大特性之一：封装
# 私有属性 private


class Person:
    __sex_list = ["GG", "MM"]

    def __init__(self, name, sex):
        if type(name) != str or type(sex) != str:
            raise TypeError("姓名和性别必须是字符串")
        self.__name = name  # 属性前面加上__代表这是一个私有属性
        self.__sex = sex

    def get_name(self):
        return self.__name

    def get_sex(self):
        return self.__sex

    def set_name(self, new_name):
        self.__name = new_name

    def set_sex(self, new_sex):
        if type(new_sex) != str or new_sex not in self.__sex_list:
            raise TypeError("性别必须是字符串")
        self.__sex = new_sex


p1 = Person("zhangsan", "GG")
p2 = Person("lisi", "MM")
# p3 = Person("lisi", 1)

# print(p1.__sex)  # 找不到
# p1.__sex = "MM"  # 找不到
print(p1.get_sex())
print(p2.get_sex())
