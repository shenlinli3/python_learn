# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/11 10:42
@Author  : zero
"""

# 索引 index

str_01 = "hello world!"
# print(len(str_01))  # 12 索引位0~11
#
# # 索引位从0开始，每次只能取一个
# print(str_01[6])  # w
# # 索引位不能越界，否则会报错
# # print(str_01[12])  # IndexError: string index out of range
# print(str_01[11])  # !
# print(str_01[-1])  # !


# # 遍历字符串
# index = 0
# while index < len(str_01):
#     print(str_01[index])
#     index += 1


# 反转字符串 !dlrow olleh
end_index = len(str_01) - 1
new_str = ""
while end_index >= 0:  # -1~-12  11~0
    # print(str_01[end_index])
    new_str += str_01[end_index]
    end_index -= 1
print(new_str)