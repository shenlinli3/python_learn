# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/13 16:44
@Author  : zero
"""

# max()  求最大
print(max([3, 2, 4, 1, 5, -2]))  # 5
print(max("YTCGVNMcxxzdvcFD"))  # z
print(max({1, 2, 3, 4}))  # 4
# min()  求最小
print(min([3, 2, 4, 1, 5, -2]))  # -2
# sum()  求和
print(sum([1, 2, 3, 4]))
print(sum((1, 2, 3, 4)))
print(sum({1, 2, 3, 4}))
# abs()  求绝对值
print(abs(10))
print(abs(-10))
# pow()  求次幂
print(pow(2, 3))
# divmod()  求整除和余的结果
print(divmod(10, 4))  # (2, 2)
print(divmod(8, 5))  # (1, 3)
# 整型转二进制
print(bin(10))  # 0b1010
# 整型转八进制
print(oct(10))  # 0o12
# 整型转16进制
print(hex(20))  # Ox14
# 根据位置取ascii码表中的字符
print(chr(65))
print(chr(97))
# 返回指定字符在ascii码表中的位置
print(ord('A'))
print(ord(' '))
# round()  四舍五入
print(round(10))
print(round(10.4))
print(round(10.5))
print(round(10.5001))