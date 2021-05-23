# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/23 11:05
@Author  : zero
"""

# 单例 singleton
import time


class Test(object):
    __instance = None
    def __new__(cls):  # 每次 Test() 就会被调用
        print(cls.__instance)
        # 这里的步骤是真正的在内存里面申请一块空间
        if cls.__instance is None:  # 判断Test类中的__instance是否是None
            time.sleep(1)
            cls.__instance = super().__new__(cls)  # 这一步是真正制造对象
        return cls.__instance

# 正常情况下，同一个类不同的实例是独立的，每个实例都有自己的内存空间
# t1 = Test()
# t2 = Test()
# t3 = Test()
# print(id(t1))
# print(id(t2))
# print(id(t3))

# 临时对象多次创建时，可能恰好在同一个地址
# print(Test())
# print(Test())
# t1 = Test()
# print(Test())
# print(Test())
# print(Test())