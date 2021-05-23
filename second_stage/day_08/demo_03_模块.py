# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/18 14:20
@Author  : zero
"""

# 模块 module
# 以文件或包为单位，把代码封装起来，便于管理，减少重复代码，优化程序结构

# 模块的分类
# 1.内置模块
# 2.自定义模块
# 3.第三方模块
    # requests

# 怎么寻找一个自定义模块呢？一般是从项目根目录开始寻找：irc_python_21
# 从起点开始，写绝对路径
# 注意：一个模块被导入时，其中的所有代码都会被执行一遍

# 1.从项目根目录一级一级导入
# import day_08.demo_04_我是自定义模块
# print(day_08.demo_04_我是自定义模块.PI)

# 2.导入并取别名
# import day_08.demo_04_我是自定义模块 as dm4
# print(dm4.PI)

# 3.from xxx import xxx
# from day_08 import demo_04_我是自定义模块
# print(demo_04_我是自定义模块.PI)
# print(demo_04_我是自定义模块.area_of_circle(2))

# 4.from xxx import xxx as xxx
# from day_08 import demo_04_我是自定义模块 as dm4
# print(dm4.PI)
# print(dm4.area_of_circle(2))

# 5.特殊的现象
# import demo_04_我是自定义模块
# print(demo_04_我是自定义模块.PI)

# 6.from xxx.xxx.xxx import xxx
from day_08.demo_04_我是自定义模块 import PI, area_of_circle
# from day_08.demo_04_我是自定义模块 import *  # 不推荐
# print(PI)
# print(area_of_circle(2))