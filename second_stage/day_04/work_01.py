# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/13 11:00
@Author  : zero
"""

# # 将url中所有参数取出并以键值对的形式装在一个字典中
# # url如下：
# # "https://iruance.com?username=admin&password=123456&sex=GG&from=China"
# # 示例输出如下：
# # {'username': 'admin', 'password': '123456', 'sex': 'GG', 'from': 'China'}
# url = "https://iruance.com?username=admin&password=123456&sex=GG&from=China"
# params = url.split("?")[1]  # username=admin&password=123456&sex=GG&from=China
# params_list = params.split("&")  # ['username=admin', 'password=123456', 'sex=GG', 'from=China']
# new_list = []
# for i in params_list:
#     new_list.append(i.split("="))  # ['username', 'admin']
# print(new_list)  # [['username', 'admin'], ['password', '123456'], ['sex', 'GG'], ['from', 'China']]
# print(dict(new_list))


# # 有这样一个字典 dic = {'python': 95, 'java': 99, 'c': 100}
# dic = {'python': 95, 'java': 99, 'c': 100}
# # 字典的长度是多少
# print(len(dic))
# # 请修改'java' 这个key对应的value值为98
# dic['java'] = 98
# print(dic)
#
# # 删除 c 这个key
# dic.pop('c')
# print(dic)
#
# # 增加一个key-value对，key值为 php, value是90
# dic['php'] = 90
# # dic.setdefault('php', 90)
# # dic.update(php=90)
# # dic.update({"php": 90})
# # dic.update([["php", 90]])
# print(dic)
#
# # 获取所有的key值，存储在列表里
# print(list(dic.keys()))
#
# # 获取所有的value值，存储在列表里
# print(list(dic.values()))
#
# # 判断 javascript 是否在字典中
# print("javascript" in dic)
#
# # 获得字典里所有value 的和
# print(sum(dic.values()))
#
# # 获取字典里最大的value
# print(max(dic.values()))
#
# # 获取字典里最小的value
# print(min(dic.values()))
#
# # 字典 dic1 = {'php': 97}， 将dic1的数据更新到dic中
# dic1 = {'php': 97}
# dic.update(dic1)
# print(dic)


students = [
    {'name': '张三', 'age': 23, 'score': 88, 'tel': '23423532', 'gender': '男'},
    {'name': '李四', 'age': 26, 'score': 80, 'tel': '12533453', 'gender': '女'},
    {'name': '王五', 'age': 15, 'score': 58, 'tel': '56453453', 'gender': '男'},
    {'name': '赵六', 'age': 16, 'score': 57, 'tel': '86786785', 'gender': '不明'},
    {'name': '小明', 'age': 18, 'score': 98, 'tel': '23434656', 'gender': '女'},
    {'name': '小红', 'age': 23, 'score': 72, 'tel': '67867868', 'gender': '女'},
]
# 打印不及格学生的名字和对应的成绩
# for i in students:
#     if i.get("score") < 60:
#         print(i.get("name"), i.get("score"))

# 统计未成年学生的个数
# kids_count = 0
# for i in students:
#     if i.get("age") < 18:
#         kids_count += 1
# print(kids_count)

# 打印手机尾号是8的学生的名字
# for i in students:
#     if i.get("tel")[-1] == "8":
#         print(i.get("name"))

# 打印最高分和对应的学生的名字 (不允许使用max和sort)
# max_score = -float("inf")
# for i in students:
#     if i.get("score") >= max_score:
#         max_score = i.get("score")
# for i in students:
#     if i.get("score") == max_score:
#         print(i.get("name"), max_score)

# 将列表按学生成绩从大到小排序
# for i in range(len(students) - 1):
#     for j in range(len(students) - 1 - i):
#         if students[j].get("score") < students[j + 1].get("score"):
#             students[j], students[j + 1] = students[j + 1], students[j]
# print(students)

# 删除性别不明的所有学生
# for i in students:
#     if i.get("gender") == "不明":
#         students.remove(i)
# print(students)


# # 不死神兔：有一对兔子，前两个月不会生育，到第三个月开始，每个月会生一对兔子，
# 假设所有的兔子都不死，问：第20月的时候，有多少对兔子
# 用代码完成
# 斐波那契数列
# 1 1 2 3 5 8 13 21 34
# first_month_count = 1
# second_month_count = 1
# for i in range(34):
#     first_month_count, second_month_count = second_month_count, first_month_count + second_month_count
#     # next_month_count = first_month_count + second_month_count  # 2
#     # first_month_count = second_month_count
#     # second_month_count = next_month_count
# print(second_month_count)


# 题目1：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
_count = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print(f"{i}{j}{k}")
                _count += 1
print(_count)


