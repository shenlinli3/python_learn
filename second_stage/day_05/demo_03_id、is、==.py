# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/14 14:43
@Author  : zero
"""

# id() 函数 返回对象在内存中的地址

# # 验证数字型 num 不可变
# num1 = 10
# num2 = 20
# num3 = 10
# print(id(num1))
# print(id(num2))
# print(id(num3))  # 和num1一致
# num1 = 30  # 改变了指向
# print(id(num1))
# print(id(num3))

# # # 验证字符串 str不可变
# str01 = "abc"
# str02 = "666"
# str03 = "abc"
# print(id(str01))
# print(id(str02))
# print(id(str03))
# str03 = "hello"  # 改变了指向
# print(id(str01))
# print(id(str03))

# # # 验证列表可变
# a = 10
# b = 20
# list01 = [10, 20]
# print(id(a))
# print(id(b))
# print(id(list01[0]))
# print(id(list01[1]))
# list01[1] = 999
# print(list01)
# print(id(list01[1]))

# 元组不可变：元组是可以变相的改变的
# tuple01 = (1, 2, 3, [4, 5])
# tuple01[3][0] = 999
# print(tuple01)  # (1, 2, 3, [999, 5])


# is 判断两个对象在内存中指向的地址是否一致
# 代码块
# 小数据池 -5~256 字符串也有缓存机制
a = 10
b = 10
print(id(a))
print(id(b))
print(a == b)  # 判断值
print(a is b)  # 判断地址