# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/12 09:01
@Author  : zero
"""

# # 创建一个空列表，命名为names，往里面添加Lihua、Rain、Jack、Xiuxiu、Peiqi和Black元素
# names = ["Lihua", "Rain", "Jack", "Xiuxiu", "Peiqi", "Black"]
#
# # 往1中的names列表里Black前面插入一个Blue
# # names.insert(5, "Blue")
# names.insert(names.index("Black"), "Blue")
# print(names)
#
# # 把names列表中Xiuxiu的名字改成中文
# # names[3] = "秀秀"
# names[names.index("Xiuxiu")] = "秀秀"
# print(names)
#
# # 往names列表中Rain后面插入一个子列表["oldboy", "oldgirl"]
# names.insert(names.index("Rain") + 1, ["oldboy", "oldgirl"])
# print(names)
#
# # 返回names列表中Peiqi的索引值（下标）
# print(names.index("Peiqi"))
#
# # 创建新列表['zero', 'karl', 'ye']，合并到names列表中
# list01 = ['zero', 'karl', 'ye']
# names.extend(list01)
# print(names)
#
# # 取出names列表中索引4~7的元素
# print(names[4:8])
#
# # 取出names列表中索引2~10的元素，步长为2
# print(names[2:11:2])
#
# # 取出names列表中最后3个元素
# print(names[-3:])
#
# # 循环names列表，打印每个元素的索引值和元素
# index = 0
# while index < len(names):
#     print(index, names[index])
#     index += 1
#
# # 循环names列表，打印每个元素的索引值和元素，当索引值为偶数时，把对应的元素改成 -1
# index = 0
# while index < len(names):
#     if index % 2 == 0:
#         names[index] = -1
#     index += 1
# print(names)


# 把1~10的所有奇数添加到一个列表并打印
# list01 = []
# index = 1
# while index <= 10:
#     if index % 2 == 1:
#         list01.append(index)
#     index += 1
# print(list01)


# 有一个列表，其中有任意个数整数，计算列表中所有数的和
# list02 = [-1, -5, 2, 4, 6, -2, 0, 9]
# index = 0
# sums = 0
# while index < len(list02):
#     sums += list02[index]
#     index += 1
# print(sums)


# 现有任意一个列表 [-1, -5, 2, 4, 6, -2, 0, 9]，完成如下需求：小于0的全部放到列表的右边，大于等于0的全部放到列表的左边，小于0的部分按照从大到小排序，大于等于0的部分按照从小到大排序
# list03 = [-1, -5, 2, 4, 6, -2, 0, 9]
# list04 = []  # 小于0
# list05 = []  # 大于等于0
# index = 0
# while index < len(list03):
#     if list03[index] < 0:
#         list04.append(list03[index])
#     else:
#         list05.append(list03[index])
#     index += 1
# list04.sort(reverse=True)
# list05.sort()
# list03 = list05 + list04
# print(list03)


# 写一个程序判断一个数字是不是回文数，回文数的概念：如12321，倒过来还是12321
# num1 = input("请输入一个数字：")
# index = 0
# while index < len(num1) // 2:  # 12321  1221
#     if num1[index] != num1[-(index + 1)]:
#         print("不是回文数")
#         break
#     index += 1
# else:
#     print("是回文数")
# if num1 == num1[::-1]:
#     print("是回文数")


# 假如有一个列表，其中有任意数字，找到该列表中最大的数与最小的数并输出
# list06 = [-1, -5, 2, 4, 6, -2, 0, 9]
# max_num = -float("inf")
# min_num = float("inf")
# index = 0
# while index < len(list06):
#     if max_num < list06[index]:
#         max_num = list06[index]
#     if min_num > list06[index]:
#         min_num = list06[index]
#     index += 1
# print(min_num, max_num)


# # 去除列表中重复的对象
# list07 = [1, 2, 3, 3, 2, 5]
# list08 = []
# index = 0
# while index < len(list07):
#     if list07[index] not in list08:
#         list08.append(list07[index])
#     index += 1
# print(list08)


# 有一个列表：['zhangsan', 'lisi', 'zhangliu', 'zhangjiu','wangwu', 'zhaoliu', 'rongqi', 'niuba']
# 将其中所有姓名以z开头的添加到一个新列表
# 将其中名字长度小于6的添加到一个新列表
# 将其中名字长度等于8的删除
# list09 = ['zhangsan', 'lisi', 'zhangliu', 'zhangjiu',
#           'wangwu', 'zhaoliu', 'rongqi', 'niuba']
# list10 = []
# list11 = []
# index = 0
# while index < len(list09):
#     if list09[index][0] == "z":
#         list10.append(list09[index])
#     if len(list09[index]) < 6:
#         list11.append(list09[index])
#     if len(list09[index]) == 8:
#         list09.pop(index)
#         # index -= 1
#         continue
#     index += 1
# print(list09)
# print(list10)
# print(list11)

print(1, 2, 3, sep="?", end="\n")
print(4, 5, 6, sep="#", end="\n")