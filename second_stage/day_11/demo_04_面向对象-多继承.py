# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/22 15:47
@Author  : zero
"""
class A:
    def test(self):
        print("test AAA")

class B:
    def test(self):
        print("test BBB")

class Animal(A):  # 动物类
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eatting")

class Flyable:
    def __init__(self, name, is_alive):
        self.name = name
        self.is_alive = is_alive
    def fly(self):
        print(f"{self.name} fly around")

class Bird(Animal, Flyable, B):  # 继承的顺序从左到右
    pass

b1 = Bird("AngryBird")
b1.eat()
b1.fly()
b1.test()  # 往上纵向（深度）查找超类中的test方法
# 在python2中是横向（广度）查找超类中的test方法