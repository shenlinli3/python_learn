# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/21 11:25
@Author  : zero
"""

import os


# 遍历指定目录下所有的文件和目录，如果是目录则再次进入并遍历
def tree(dir_path):
    for i in os.listdir(dir_path):
        i = os.path.join(dir_path, i)
        print(i)
        if os.path.isdir(i):
            tree(i)
# tree(r"D:\PythonProjects")


# 统计指定目录下所有文件和目录的数量，包括下一级目录中的文件和目录
# def file_and_dir_count(dir_path):
#     file_count = 0
#     dir_count = 0
#     for i in os.listdir(dir_path):
#         i = os.path.join(dir_path, i)
#         if os.path.isdir(i):
#             dir_count += 1
#             res = file_and_dir_count(i)
#             file_count += res["file_count"]
#             dir_count += res["dir_count"]
#         else:
#             file_count += 1
#     return {"file_count": file_count, "dir_count": dir_count}
#     # print({"file_count": file_count, "dir_count": dir_count})
# print(file_and_dir_count(".."))


# 查询指定目录下所有包含指定文件名的文件的路径
# def find_file(dir_path, filename):
#     for i in os.listdir(dir_path):
#         i = os.path.join(dir_path, i)
#         if os.path.isdir(i):
#             find_file(i, filename)
#         else:
#             if filename in os.path.split(i)[-1]:
#                 print(i)
# find_file("..", "work")