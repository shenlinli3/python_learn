# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/22 10:31
@Author  : zero
"""

# 类-实例  class-instance
# class Person:  # 理解为一个模板
#     pass
#
# print(Person)  # <class '__main__.Person'>
#
# p1 = Person()  # 按照模板制造出来一个人  类实例化
# print(p1)  # <__main__.Person object at 0x00000123FCA388C8>
# p2 = Person()
# print(p2)  # <__main__.Person object at 0x0000020F37388A48>


# # 给对象手动绑定属性
# class Student:
#     pass
#
# s1 = Student()
# s2 = Student()
# s1.name = "zhangsan"  # 给对象赋予属性
# s2.name = "lisi"  # 给对象赋予属性
# print(s1.name)
# print(s2.name)
# s1.age = 18
# print(s1.age)
# print(s2.age)


# # 类属性和对象的属性 要区分开
# class Animal:
#     come_from = "Earth"
#
# a1 = Animal()
# a2 = Animal()
# print(a1.come_from)
# print(a2.come_from)
# a1.come_from = "China"
# print(a1.come_from)  # 类和对象都有这个属性，先找对象的
# print(a2.come_from)
# del a1.come_from
# print(a1.come_from)  # 对象没有某个属性，回去类里面找
# print(a2.come_from)
# Animal.food = "竹子"
# print(Animal.food)
# print(a1.food)
# print(a2.food)


# 类的初始化方法
# class Person:
#     come_from = "Earth"
#     def __init__(self, name, age):  # 在类实例化的时候会自动执行，self会自动接收到当前实例化的对象
#         self.name = name
#         self.age = age
#
# p1 = Person("zhangsan", 18)  # p1.name = "zhangsan"     p1.age = 18
# p2 = Person("lisi", 3)  # p2.name = "lisi"    p2.age = 3
# print(p1.name)
# print(p2.name)
# print(p1.age)
# print(p2.age)

# 怎么实现 统计学生类被实例化的次数
# class Student:
#     _count = 0
#     def __init__(self):
#         Student._count += 1
#
# s1 = Student()
# s2 = Student()
# s3 = Student()
# print(Student._count)


# 给对象加上行为
class Person:
    come_from = "Earth"
    def __init__(self, name, age, sex="未知", address=None):
        self.name = name
        self.age = age
        self.sex = sex
        self.address = address
    def eat(self, food):  # 哪个实例执行eat，self就指向这个实例
        print(f"{self.name} is eatting {food}")
    def sing(self):  # 哪个实例执行eat，self就指向这个实例
        print(f"{self.name} is singing")

p1 = Person("zs", 18, "GG")
p2 = Person("ls", 17, "MM")
print(p1.name, p1.age, p1.sex)
print(p2.name, p2.age, p2.sex)
p1.eat("苹果")
p2.eat("香蕉")
p2.sing()