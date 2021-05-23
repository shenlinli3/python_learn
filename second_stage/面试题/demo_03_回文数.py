# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/21 09:04
@Author  : zero
"""

# def is_palindromic_num(num: int) -> bool:
#     """使用str()加切片反转的方式判断是否是回文数
#     :param num: 任意整数
#     :return: 如果是回文数返回True 否则False
#     """
#     return num >= 0 and str(num) == str(num)[::-1]


# def is_palindromic_num(num: int) -> bool:
#     """完全使用算术计算完成
#     :param num:
#     :return:
#     """
#     if not (isinstance(num, int) and num >= 0):
#         return False
#     if num < 10:  # 0~9直接返回True
#         return True
#     temp_num = num  # 临时数字，被用于每次取个位数
#     reverse_num = 0  # 反转之后的数字
#     while temp_num >= 10:
#         # 假设现在参数num = temp_num = 123
#         # reverse_num第一轮 0 * 10 + 123 % 10 = 3
#         # reverse_num第二轮 3 * 10 + 12 % 10 = 32
#         reverse_num = reverse_num * 10 + temp_num % 10
#
#         # temp_num第一轮 123 // 10 = 12
#         # temp_num第二轮 12 // 10 = 1
#         temp_num = temp_num // 10
#     # 循环结束，temp_num此时变成个位数
#     reverse_num = reverse_num * 10 + temp_num  # 得到num反转之后的结果
#     return num == reverse_num


# def is_palindromic_num(num: int) -> bool:
#     """把数字的每一位利用求余放入到列表，最后对比列表的各索引位
#     如num_list[0]==num_list[-1]  num_list[1]==num_list[-2]  num_list[2]==num_list[-3]"""
#     if not (isinstance(num, int) and num >= 0):
#         return False
#     if num < 10:  # 0~9直接返回True
#         return True
#     num_list = []
#     while num >= 10:
#         num_list.append(num % 10)  # 添加num的个位数到列表中
#         num //= 10  # num去除一次个位
#     num_list.append(num)
#     for i in range(len(num_list) // 2):
#         if num_list[i] != num_list[-i - 1]:
#             return False
#     else:
#         return True


def is_palindromic_num(num: int) -> bool:
    """使用str()把数字转为字符串再判断前后索引位对应数字是否相同
    如num_list[0]==num_list[-1]  num_list[1]==num_list[-2]  num_list[2]==num_list[-3]"""
    if not (isinstance(num, int) and num >= 0):
        return False
    if num < 10:  # 0~9直接返回True
        return True
    num_str = str(num)
    for i in range(len(num_str) // 2):
        if num_str[i] != num_str[-i - 1]:
            return False
    return True


print(is_palindromic_num(10.5))  # False
print(is_palindromic_num("abc"))  # False
print(is_palindromic_num(-1))  # False
print(is_palindromic_num(0))  # True
print(is_palindromic_num(123))  # False
print(is_palindromic_num(12321))  # True
print(is_palindromic_num(1221))  # True
