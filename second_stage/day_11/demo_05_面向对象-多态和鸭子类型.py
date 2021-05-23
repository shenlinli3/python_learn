# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/22 16:08
@Author  : zero
"""
# 多态：在面向对象中，一个类的实例可以是多种形态（向上转型）
# 鸭子类型：在python中，只要一个对象长的像鸭子，走路和鸭子差不多，我就认为它是一只鸭子

class Person:  # 会默认继承自object类
    def eat(self):
        print("eat eat eat")

class Student(Person):
    pass

class LowLevelStudent(Student):
    pass

p1 = Person()
s1 = Student()
lls1 = LowLevelStudent()
# # isinstance 判断指定对象是否是指定类的实例
# print(isinstance(p1, Person))  # True
# print(isinstance(p1, Student))  # False
# print(isinstance(s1, Student))  # True
# print(isinstance(s1, Person))  # True
# print(isinstance(lls1, LowLevelStudent))  # True
# print(isinstance(lls1, Student))  # True
# print(isinstance(lls1, Person))  # True
print(type(lls1) == Student)
print(type(lls1) == LowLevelStudent)

# 通过上面的验证，我们可知：在面向对象中，一个类的实例可以是多种形态（向上转型）

# p1.eat()
# s1.eat()
# lls1.eat()

class Pig:
    def eat(self):
        print("eat eat eat")

def double_eat(obj: Person):
    obj.eat()
    obj.eat()

# double_eat(p1)
# double_eat(s1)
# double_eat(lls1)
pig1 = Pig()
double_eat(pig1)
# double_eat(Pig())  # 这里Pig的实例对象没有名字，一般我们称之为 匿名对象