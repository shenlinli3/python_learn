# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/18 11:43
@Author  : zero
"""

# zip() 把多个序列中同一索引位的元素组合到一个元组中
list01 = [1, 2, 3]
list02 = ["a", "b", "c", "d"]
list03 = ["666", "777", "888"]
print(list(zip(list01, list02, list03)))
print(dict(zip(list01, list02)))

# enumerate()  把列表中元素变成 (当前元素索引, 当前元素)
list04 = ["666", "777", "888"]
print(list(enumerate(list04)))
for index, i in enumerate(list04, start=1):
    print(index, i)

# reversed()  反转序列
print(list(reversed([1, 2, 3])))

# eval()  把字符串当成python代码来执行
print(eval("1 + 1"))

# callable()  判断一个对象是否可调用
def f1():
    print("f1")
f1()  # 加括号 就是调用
print(callable(f1))
a = f1
print(callable(a))
b = str(123)
print(b())
print(callable(b))