# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/12 11:24
@Author  : zero
"""
# # 把字符串中的每一个单词首字母大写
# s = "hello world hello python"
# print(s.title())
# new_s = ""
# # "Hello World Hello Python"
# s_list = s.split()  # 默认根据空格切割，得到一个列表，里面装着四个单词
# print(s_list)
# index = 0
# while index < len(s_list):
#     new_s += s_list[index].capitalize() + " "
#     index += 1
# s = new_s.strip()
# print(s)


# # 基础练习
# # 将字符串 "abcd" 转成大写
# print("abcd".upper())
# # 计算字符串 "cd" 在 字符串 "abcd"中出现的位置
# print("abcd".index("cd"))
# # 字符串 "a,b,c,d" 请根据逗号切割字符串，分割后的结果是什么类型的？
# print("a,b,c,d".split(","))
# # "Python is good" 请将字符串里的Python替换成 java ，并输出替换后的结果
# print("Python is good".replace("Python", "java"))
# # "irc_python_19.py.xxx" 请写程序从这个字符串里获得.py前面的部分（用至少两种方式）
# print("irc_python_19.py.xxx".split(".py")[0])
# print("irc_python_19.py.xxx"[:"irc_python_19.py.xxx".index(".py")])
# # "this is a book" 请用程序取出该英文句子的第一个单词并打印
# print("this is a book".split()[0])
# # "this is a book" 请用程序判断该字符串是否以apple结尾
# print("this is a book".endswith("apple"))
# # "This IS a book" 请将字符串里的大写字符转成小写字符
# print("This IS a book".lower())
# # "this is a book\n" 字符串的末尾有一个回车符，请将其删
# print("this is a book\n".strip())


# 有一个英文句子，比如 'hello world hello python'，将其中的每一个单词首字母大写
# str01 = 'hello world hello python'
# str02 = ''
# list01 = str01.split()
# for i in list01:
#     str02 += (i.capitalize() + " ")
# str01 = str02.strip()
# print(str01)


# 有一个字符串HellO WorlD，将字符串中所有的小写字母转大写，大写字母转小写
# str03 = ''
# for i in "HellO WorlD":
#     if i.isupper():
#         str03 += i.lower()
#     else:
#         str03 += i.upper()
# print(str03)


# # 写一个程序，接收用户输入任意内容，然后判断该内容中的英文、数字、空白符、其它字符分别有多少
# any_str = input("请输入：")
# alpha_count = num_count = space_count = other_count = 0
# for i in any_str:
#     if i.isalpha() and i.isascii():
#         alpha_count += 1
#     elif i.isdigit():
#         num_count += 1
#     # elif i.isspace():
#     elif i == " ":
#         space_count += 1
#     else:
#         other_count += 1
# print("英文：{}  数字：{}  空格：{}  其它：{}"
#       .format(alpha_count, num_count, space_count, other_count))


# 输入用户名，判断用户名是否合法(用户名必须包含且只能包含数字和字母，并且第一个字符必须是大写字母)
# username = input("请输入用户名：")
# if username.isalnum() and username.isascii() and username[0].isupper():
#     print("合法")
# else:
#     print("非法")


# 输入一个字符串，将字符串中所有的数字字符取出来产生一个新的字符串
# any_str = input("请输入：")
# new_str = ''
# for i in any_str:
#     if i.isdigit():
#         new_str += i
# print(new_str)


# 给定一个英文句子比如"hello python" 将句子中的单词位置反转为 "python hello"
# print(" ".join("hello python".split()[::-1]))


# 假设有任意字符串如："hello world"，写程序把字符串中所有l出现的索引位加入到一个列表，如[2, 3, 9]
# str01 = "hello world"
# list01 = []
# for i in range(len(str01)):
#     if str01[i] == 'l':
#         list01.append(i)
# print(list01)


# 有一个url：https://iruance.com?username=admin&password=123456&sex=GG&from=China，
# 将url中所有参数值取出并装在一个列表中，如['admin', '123456', 'GG', 'China']
url = "https://iruance.com?username=admin&password=123456&sex=GG&from=China"
new_list = []
# ['https://iruance.com', 'username=admin&password=123456&sex=GG&from=China'][1]
params = url.split("?")[1]  # username=admin&password=123456&sex=GG&from=China
params_list = params.split("&")  # ['username=admin', 'password=123456', 'sex=GG', 'from=China']
for i in params_list:
    new_list.append(i.split("=")[1])
print(new_list)