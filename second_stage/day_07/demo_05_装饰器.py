# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/17 15:53
@Author  : zero
"""

import time  # 导入时间模块

# 装饰器 decorator
# 作用：不修改代码的前提下，给程序增加一些功能
# 非常符合编程六大原则之一，开放封闭原则
# 面向扩展开放（可以非常方便的增加新功能）
# 面向修改封闭（源代码一般不能修改）


###### 1.
# 假如现在我有任意一个函数，已经在使用
# def f1():
#     print("f1 函数开始")
#     time.sleep(1)
#     print("f1 函数结束")
#
# # f1()
# # f1()
# # f1()
# # 我希望给这个函数增加一点功能：执行前后打印当前时间
# # 这样需要修改原有的代码
# print(f"开始时间：{time.time()}")
# f1()
# print(f"结束时间：{time.time()}")
# print(f"开始时间：{time.time()}")
# f1()
# print(f"结束时间：{time.time()}")
# print(f"开始时间：{time.time()}")
# f1()
# print(f"结束时间：{time.time()}")


###### 2.写一个装饰器，给函数执行前后加上了一些功能，但是发现没有返回值
# def exe_time(func):
#     def wrapper():
#         # 执行前要增加的功能
#         print(f"开始时间：{time.time()}")
#         func()
#         # 执行后要增加的功能
#         print(f"结束时间：{time.time()}")
#     return wrapper
#
# @exe_time  # 相当于在55行执行了 f2 = exe_time(f2)
# def f2():
#     print("f2 函数开始")
#     time.sleep(1)
#     print("f2 函数结束")
# # f2 = exe_time(f2)  # 实际上这里的f2是wrapper
#
# f2()
# f2()
# f2()


###### 3.给被装饰的函数增加返回值
# def exe_time(func):
#     def wrapper():
#         # 执行前要增加的功能
#         print(f"开始时间：{time.time()}")
#         res = func()  # 先获取执行结果
#         # 执行后要增加的功能
#         print(f"结束时间：{time.time()}")
#         return res  # 执行上面增加的功能之后再返回
#     return wrapper
#
# @exe_time  # 相当于在55行执行了 f3 = exe_time(f3)
# def f3():
#     print("f3 函数开始")
#     time.sleep(1)
#     print("f3 函数结束")
#     return "我是f3的返回值"
# # f3 = exe_time(f3)  # 实际上这里的f3是wrapper
# print(f3())
# print(f3())
# print(f3())


###### 4.给被装饰的函数增加参数
# 因为我们不知道，被装饰的函数会有怎样的参数，我们得实现一个通用的参数传递
# def exe_time(func):
#     def wrapper(*args, **kwargs):  # (1, 2, 3, k1="v2", k2="v2")
#         # 执行前要增加的功能
#         print(f"开始时间：{time.time()}")
#         res = func(*args, **kwargs)  # 先获取执行结果
#         # 执行后要增加的功能
#         print(f"结束时间：{time.time()}")
#         return res  # 执行上面增加的功能之后再返回
#     return wrapper
#
# @exe_time  # 相当于在55行执行了 f4 = exe_time(f4)
# def f4(_str):
#     print(f"f4 函数开始 {_str}")
#     time.sleep(1)
#     print(f"f4 函数结束 {_str}")
#     return "我是f4的返回值"
#
# @exe_time
# def f5(s1, s2):
#     print(f"f5 函数开始 {s1 + s2}")
#     time.sleep(1)
#     print(f"f5 函数结束 {s1 + s2}")
#     return "我是f5的返回值"
#
# # print(f4("python"))  # 这里执行的f4就是wrapper
# # print(f4("python"))
# # print(f4("python"))
#
# print(f5("hello", "python"))  # 这里执行的f5就是wrapper
# print(f5("hello", "python"))
# print(f5("hello", "python"))


###### 5.给被装饰的函数增加调用次数统计
def exe_time(func):
    exe_count = 0
    def wrapper(*args, **kwargs):  # (1, 2, 3, k1="v2", k2="v2")
        # 执行前要增加的功能
        print(f"开始时间：{time.time()}")
        res = func(*args, **kwargs)  # 先获取执行结果
        # 执行后要增加的功能
        print(f"结束时间：{time.time()}")
        nonlocal exe_count
        exe_count += 1
        print(f"{func.__name__} 函数被执行了{exe_count}次")
        return res  # 执行上面增加的功能之后再返回
    return wrapper

@exe_time  # 相当于在55行执行了 f4 = exe_time(f4)
def f4(_str):
    print(f"f4 函数开始 {_str}")
    time.sleep(1)
    print(f"f4 函数结束 {_str}")
    return "我是f4的返回值"

print(f4("python"))  # 这里执行的f4就是wrapper
print(f4("python"))
print(f4("python"))