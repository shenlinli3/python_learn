# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/21 09:11
@Author  : zero
"""

# 一.os Operating System
import os
# # 1. os.listdir()  linux: ls
# print(os.listdir())  # 默认列出当前目录下所有文件和文件夹
# print(os.listdir("D:/PythonProjects/irc_python_21"))
# # 2. os.getcwd()  linux: pwd
# print(os.getcwd())
# # 3. os.chdir()  linux: cd
# os.chdir("E:/")
# print(os.listdir())
# # 4. os.mkdir()  linux: mkdir
# os.mkdir("test_dir_01")
# # 5. os.rmdir()  linux: rm
# os.rmdir("test_dir_01")
# # 6. os.makedirs()
# os.makedirs("a/b/c")  # mkdir -p a/b/c
# # 7. os.removedirs()  linux: rm
# os.removedirs("a/b/c")
# # 8. os.remove()  linux: rm
# os.remove("1.txt")
# # 9. os.rename()  linux: mv
# os.rename("2.txt", "1.txt")
# # 10. os.cpu_count() 实际上在win上，是统计核心线程数（双核四线程就是4）
# print(os.cpu_count())

# # 11. os.path.curdir  # 当前所在目录
# print(os.path.curdir)  # .
# # 12. os.path.pardir()  # 当前所在目录的父级目录
# print(os.path.pardir)  # ..
# # 13. os.path.abspath()  # 返回指定目录的绝对路径
# print(os.path.abspath(os.path.curdir))
# print(os.path.abspath(os.path.pardir))
# # 14. os.path.exists()  # 判断指定路径是否存在
# print(os.path.exists("1.txt"))
# print(os.path.exists("2.txt"))
# # 15. os.path.isdir()  # 判断指定路径是否是文件夹，文件夹不存在也返回False
# print(os.path.isdir("test_dir"))
# print(os.path.isdir("1.txt"))
# print(os.path.isdir("2.txt"))
# # 16. os.path.isfile()  # 判断指定路径是否是文件，文件不存在也返回False
# print(os.path.isfile("test_dir"))
# print(os.path.isfile("1.txt"))
# print(os.path.isfile("2.txt"))
# # 17. os.path.split()  # 切割路径
# print(os.path.split(__file__))
# # 18. os.path.join()  # 拼接路径
# print(os.path.join("E:\\", "a", "b", "c", "test.txt"))
# # print(os.path.join("/", "a", "b", "c", "test.txt"))  #linux: /a/b/c/test.txt


# 二.sys python系统
import sys
# # 1.sys.platform 查询python运行的平台
# print(sys.platform)
# # 2.sys.version 查询python解释器的版本信息
# print(sys.version)
# # 3.sys.exit()
# sys.exit()  # 程序退出
# 4.sys.argv  命令行参数
# print(sys.argv)  # 第一个值默认是当前文件本身
# if len(sys.argv) > 1:
#     if sys.argv[1] == "test":
#         print("测试环境！")
#     elif sys.argv[1] == "prod":
#         print("生产环境！")
# 5.设置和查看递归最大次数
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(20)
# print(sys.getrecursionlimit())