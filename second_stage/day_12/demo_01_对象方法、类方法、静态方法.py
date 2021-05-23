# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/23 10:22
@Author  : zero
"""

# 对象方法
# class Test:
#     def __init__(self, _id):
#         self._id = _id
#
#     def f1(self):  # 第一个参数必须是self，传进来的self必须是当前类的实例，这就叫做对象方法
#         print(f"{self._id} f1")
#
# t1 = Test(1)
# t2 = Test(2)
# t1.f1()
# t2.f1()
# Test(3).f1()  # 匿名对象调用
# # Test.f1()  # 这里缺少了一个self对象，会报错



# # 类方法
# class Test:
#     name = "我是Test类"
#
#     @classmethod
#     def f1(cls):  # 第一个参数必须是cls，cls是当前类或者当前类的实例，这叫做类方法
#         print(cls.name)
#
# Test.f1()  # 使用类调用
# t1 = Test()
# t1.f1()  # 使用对象调用



# 静态方法
class Test:

    @staticmethod
    def f1():  # 除了要通过类名调用，和普通的函数没有任何区别
        print("我是f1")

Test.f1()


# 简单总结：
# 对象方法只能使用对象调用
# 类方法可以使用类或对象调用
# 静态方法不需要任何类或对象，只是需要通过类名去找到它