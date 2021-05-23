# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/21 09:07
@Author  : zero
"""

# 阿里伯乐面试题 有个键盘，只有a-z的26个应为字母的输入按键，现在键盘有两个按键坏了
# 按键i，会退格，效果相当于常规键盘的backspace（删除键）
# 按键o，会撤回上一步操作，相当于win操作系统上的ctrl+z
# 实现一个方法，模拟键盘的输出逻辑
# 例1：输入 fineiamok -> 输出nak
# 例2：输入 zio -> 输出z
# 如果输入 thismayi -> 输出?

# 这道题看了仔细想了一下，可以在面试的时候问一下面试官ctrl+z要的效果
# 比如输入abcoo
# 第一种是：会撤回之前的任何一次操作，包括撤回
#     abc 撤回变成 ab 然后又一个撤回 撤回之前的撤回操作 重新变成abc
# 第二种是：只撤回之前的非撤回操作
#     abc撤回变成 ab 又撤回变成 a


def bad_keyboard(_str):
    """连续输入o时，会撤回上一次的撤回操作"""
    output_str = ""
    backup_str = ""
    for s in _str:
        if s == "o":  # 每次输入o，交换新旧字符串
            output_str, backup_str = backup_str, output_str
        else:
            backup_str = output_str  # 备份当前字符串
            # 如果输入i则字符串去除最后一位，否则加上当前新输入的字符串
            output_str = output_str[:-1] if s == "i" else output_str + s
    return output_str


print(bad_keyboard("fineiamok"))  # nak
print(bad_keyboard("fineiamook"))  # namk
print(bad_keyboard("fineiamoook"))  # nak
print(bad_keyboard("zio"))  # z
print(bad_keyboard("thisismayi"))  # tsma


def bad_keyboard(_str):
    """连续输入o时，只会撤回上一次的非撤回操作"""
    output_str = ""
    while _str.find("o") != -1:
        _str = _str[:_str.find("o") - 1] + _str[_str.find("o") + 1:]
    for s in _str:
        output_str = output_str[:-1] if s == "i" else output_str + s
    return output_str


print(bad_keyboard("fineiamok"))  # nak
print(bad_keyboard("fineiamook"))  # nk
print(bad_keyboard("fineiamoook"))  # nek
print(bad_keyboard("ziioo"))  # z
print(bad_keyboard("thisismayi"))  # tsma
print(bad_keyboard("abcdiooo"))  # ab
