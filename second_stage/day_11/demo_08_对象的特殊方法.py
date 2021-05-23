# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/22 17:46
@Author  : zero
"""
# 重写 __str__
# class Test:
#     def __init__(self, t):
#         self.t = t
#
#     def __str__(self):
#         return f"Test t: {self.t}"
#
# t1 = Test("a")
# t2 = Test("b")
# print(t1)  # <__main__.Test object at 0x0000026765698FC8>
# print(t2)


# 重写 __str__ 和 __repr__
# class Student:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def __str__(self):
#         return f"""Student {self.name, self.age, self.sex}"""
#     __repr__ = __str__
#
# s1 = Student("张三", 18, "GG")
# print(s1)
# s2 = Student("李四", 99, "MM")
# print(s2)

# 重写 __len__
# 在python中除了数字型，所有的基础数据类型都可以使用len()函数
# class Person:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#
#     def __len__(self):
#         return self.height
#
# p1 = Person("zero", 188)
# print(len(p1))
# p2 = Person("zhangsan", 166)
# print(len(p2))


# 想要对一个对象实现索引、切片、键 取值，就要实现__getitem__方法
# class Test:
#
#     def __getitem__(self, item):
#         print(f"__getitem__收到的值：{item}")
#         return 666
# t1 = Test()
# print(t1[-1])
# print(t1["a"])
# print(t1[1, 3])
# list01 = [1, 2, 3, 4, 5]
# print(list01[-1])


# 重写两个对象判断是否相等的逻辑 __eq__
class Equal:
    def __eq__(self, other):
        print(other)  # e2
        if other == 666:
            return True
        else:
            return False
    pass

e1 = Equal()
print(e1 == 10)
print(e1 == "abc")
e2 = Equal()
print(e2)
print(e1 == e2)
print(e1 == None)
print(e1 == 666)