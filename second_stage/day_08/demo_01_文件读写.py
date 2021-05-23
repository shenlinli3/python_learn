# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/18 09:54
@Author  : zero
"""

import time

# open() 打开
# file 文件：要读写的文件的路径
# mode 模式：打开的模式
    # r-read-读
    # w-write-写
    # a-append-追加
# buffering 缓冲区
# encoding 编码格式


# # 读模式 r 文件找不到会报错
# # fr = open("test_r.txt", "r", encoding="utf-8")
# # fr = open("../test_r.txt", "r", encoding="utf-8")
# fr = open(
#     # file="D:/PythonProjects/irc_python_21/day_08/test_r.txt",
#     # file=r"D:\PythonProjects\irc_python_21\day_08\test_r.txt",
#     file="D:\\PythonProjects\\irc_python_21\\day_08\\test_r.txt",
#     mode="r",
#     encoding="utf-8"
# )
# read_res = fr.read()
# print(read_res)
# fr.close()


# # 写模式 w 文件不存在会创建，会先把文件中的内容清空再写入
# fw = open(
#     file="test_w.txt",
#     mode="w",
#     encoding="utf-8"
# )
# fw.write("test_w_666\n")  # write() 并不是直接把内容写入到文件中，而是写入到缓冲区
# fw.write("test_w_777")
# fw.flush()  # 把缓冲区中的内容真正写入到文件
# fw.close()  # 释放文件句柄的时候会自动flush()


# # 追加模式 a 如果文件不存在则会新建，会把内容追加到文件的末尾
# fa = open("test_a.txt", "a", encoding="utf-8")
# fa.write("666\n")
# fa.write("777\n")
# fa.close()


# # 字节读取模式 rb 注意：没有编码格式
# frb = open(
#     file=r"C:\Users\zero\Desktop\test.jpg",
#     mode="rb"
# )
# read_res = frb.read()
# frb.close()
# print(read_res)
# # 字节写入模式 wb
# frw = open("test.jpg", "wb")
# frw.write(read_res)
# frw.close()


# + 模式 r+ 读+写
# fr = open("test_r.txt", "r+", encoding="utf-8")
# print(fr.read())  # 一次性读完，指针走到末尾
# fr.write("666")  # io.UnsupportedOperation: not writable
# fr.close()

# # w+ 写+读
# fw = open("test_w.txt", "w+", encoding="utf-8")
# fw.write("test66666你好")  # 此时指针在文件末尾
# fw.seek(0, 0)  # 调整指针的位置，按照字节调整
# print(fw.read())
# print(fw.tell())  # 获取指针的位置
# fw.close()


# 推荐的open写法
with open("test_r.txt", "r", encoding="utf-8") as fr:
    print(fr.read())