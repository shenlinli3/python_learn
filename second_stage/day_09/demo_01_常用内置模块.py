# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/19 10:29
@Author  : zero
"""


# 一. json 序列化模块
import json
python_obj = [1, True, "abc", {"k1": "v1"}, (1, 2, 3)]
print(python_obj)
print(type(python_obj))
# 把python对象转换为json字符串
json_str = json.dumps(python_obj)
print(json_str)
print(type(json_str))
# 把json字符串转换为python对象
python_obj1 = json.loads(json_str)
print(python_obj1)
print(type(python_obj1))