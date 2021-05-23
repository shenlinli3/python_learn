# 与 或 非
# and or not

# # and 一假则假 全真则真
# print(True and True and True)
# print(True and True and False)
# # or 一真则真 全假则假
# print(False or False or False)
# print(False or True or False)
# # not 取反
# print(not True)
# print(not False)

# 优先级：not > and > or
# 验证优先级 not > and
print(True and not False)
# 验证优先级 and > or
print(True or True and False)


# 1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# F or T or F and T and T or F
# F or T or F or F
# T
print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)

# not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# not T and T or F and T and T or F
# F and T or F and T and T or F
# F or F or F
# F
print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)