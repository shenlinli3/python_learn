# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/11 14:13
@Author  : zero
"""

# 列表 list

# # 列表的初始化
# # 1.初始化一个列表并放入对象
# list01 = [1, 9.9, True, "abc"]
# print(type(list01))
# print(list01)
# # 2.初始化一个空列表
# list02 = []
# print(list02)
# # 3.初始化一个空列表
# list03 = list()
# print(list03)
# # 4.打散一个字符串并放入一个列表
# list04 = list("hello")
# print(list04)



# # 列表-查
# list05 = [1, 9.9, True, "abc", [1, 2, 3]]
# # 1.查询列表的长度
# print(len(list05))  # 5
#
# # 2.根据索引查
# print(list05[2])
#
# # 3.根据切片查，切出来的依然是一个列表
# print(list05[1:4])
#
# # 4. list.index() 查询指定对象在列表中的位置
# print(1 == True)
# print(list05.index(True))  # 0
# print(list05.index(True, 1))  # 2
# # print(list05.index(False))  # 对象不存在会报错
#
# # 5. list.count() 查询指定对象在列表中出现的次数
# print(list05.count(True))
# print(list05.count(False))


# # 列表-增
# list06 = []
# # 1. list.append() 追加一个对象到列表的末尾
# list06.append(1)
# list06.append(True)
# print(list06)
#
# # 2. list.insert() 把一个对象插入到列表的指定位置
# list06.insert(0, "abc")
# print(list06)
#
# # 3. list.extend() 合并一个可迭代对象
# list06.extend([777, 888])
# list06.extend("abc")
# print(list06)


# # 列表-改
# list07 = ['abc', 1, True, 777, 888, 'a', 'b', 'c']
# # 1.根据索引改
# list07[2] = False
# print(list07)
#
# # 2.根据切片改
# # list07[1:5] = 1, 2, 3
# list07[1:1] = "121"
# print(list07)


# # 列表-删
list08 = ['abc', 1, True, 777, 888, 'a', 'b', 'c']
# # 1. list.pop()  删除指定索引位的对象并返回被删除的对象，默认删除最后一位
# print(list08.pop())
# print(list08.pop(2))
# print(list08)
#
# # 2. list.remove()
# list08.remove(888)
# print(list08)
#
# # 3. del
# del list08[1]
# print(list08)
# del list08[2:]
# print(list08)
#
# # 4. list.clear()  清空列表
# list08.clear()
# print(list08)


# 列表的其它操作
# 1.列表的成员运算
print(1 in [1, 2, 3])
# 2.列表可以和列表相加
print([1, 2, 3] + [4, 5])
# 3.列表可以和整型相乘
print([1, 2, 3] * 3)
# 4. list.sort() 列表的排序
list09 = [1, 9, -2, 3, 8, -4, 5, -6, 7]
# list09.sort()  # 正序
# list09.sort(reverse=True)  # 倒序
# print(list09)
# 5. list.reverse() 反转列表
list09.reverse()
print(list09)