# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/18 14:31
@Author  : zero
"""

PI = 3.1415926  # 常量


def area_of_circle(r):
    """计算圆的面积"""
    return PI * r ** 2


def weight_of_circle_zhu(r, h):
    """计算圆柱的体积"""
    return PI * r ** 2 * h


print("我是自定义模块中的print")


if __name__ == "__main__":
    print(area_of_circle(2))
    print(weight_of_circle_zhu(2, 2))
    print(globals())