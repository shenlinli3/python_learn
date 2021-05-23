# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/22 14:25
@Author  : zero
"""

# 子类会继承父类的属性和方法，包括初始化方法
# 私有属性、方法是不能继承的
# 如果子类调用某个方法的时候，自己这个类有这个就调用自己的，否则调用父类的

class Animal:
    def __init__(self, name, sex):
        self.name = name
        self.__sex = sex
    def eat(self):
        print(f"{self.name} is eatting")
    def get_sex(self):
        print(self.__sex)

class Pig(Animal):
    # def __init__(self, name, sex, age):
    #     # super代表父类
    #     super().__init__(name, sex)
    #     self.name = name
    #     self.__sex = sex
    #     self.age = age
    #     print(dir(self))
    def eat(self):
        print(f"{self.name} is eatting 白菜")

# peiqi = Pig("peiqi", "MM")
# peiqi.eat()
# peiqi.get_sex()
# print(dir(peiqi))

# 多层继承
class HomePig(Pig):
    pass

hp1 = HomePig("乔治", "GG")
hp1.eat()