# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/13 15:37
@Author  : zero
"""

# 条件判断分支
num1 = int(input("第一个数："))
num2 = int(input("第二个数："))
# if num1 > num2:
#     print(num1)
# else:
#     print(num2)
print(num1 if num1 > num2 else num2)

# printf("%d", num1 > num2 ? num1 : num2)  # c
# alert(num1 > num2 ? num1 : num2);  # js