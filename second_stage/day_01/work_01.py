# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/10 17:07
@Author  : zero
"""

# 1.用户输入任意两个数，比如10 95或95 10，计算它们（都包含）之间所有数的和
# num1 = int(input("请输入第一个数："))
# num2 = int(input("请输入第二个数："))
# if num1 > num2:
#     # 交换两个变量
#     num3 = num1
#     num1 = num2
#     num2 = num3
# sums = 0
# while num1 <= num2:
#     sums += num1
#     num1 += 1
# print(sums)


# 2.求出1-1000所有奇数的和以及偶数的和
# start_num = 1
# even_sum = 0
# odd_sum = 0
# while start_num <= 1000:
#     if start_num % 2 == 0:
#         odd_sum += start_num
#     else:
#         even_sum += start_num
#     print(start_num)
#     start_num += 1
# print(even_sum, odd_sum)


# 3.用户输入任意一个数，计算从1到该数的乘积
# start = 1
# end = int(input("请输入一个数："))
# sums = 1
# while start <= end:
#     sums *= start
#     start += 1
# print(sums)


# 4.求出100-999中所有的水仙花数，水仙花数的定义：比如153 ：1 ** 3 + 5 ** 3 + 3 ** 3 = 153，
# 也就是说每一位的数拿出的三次方相加正好等于这个数本身
# start_num = 100
# while start_num <= 999:
#     x = (start_num // 100) ** 3
#     y = (start_num // 10 % 10) ** 3
#     z = (start_num % 10) ** 3
#     if x + y + z == start_num:
#         print(start_num)
#     start_num += 1


# 5.写一个猜谜游戏，先定义好一个数，程序开始运行后总共有十次机会猜，猜对了则提示中奖了并结束程序，猜错了则提示太大了或太小了并给出剩余次数
# 生成随机数的方法：比如1~100随机
# import random
# pass_num = random.randint(1, 100)
# # print(pass_num)
# guess_count = 0
# while guess_count < 10:
#     guess_count += 1
#     guess_num = int(input("请输入一个数："))
#     if guess_num > pass_num:
#         print("猜大了，还有%d次机会" % (10 - guess_count))
#     elif guess_num < pass_num:
#         print("猜小了，还有%d次机会" % (10 - guess_count))
#     else:
#         print("猜对了，没有奖！")
#         break


# 6.完成一个登录系统，总共可登录失败三次，用户输入用户名和密码，
# 如果用户名为admin密码为123456则提示登录成功，否则提示登录失败，
# 并给出剩余登录次数，登录错误次数三次则提示账号被锁定！
# login_count = 0
# while login_count < 3:
#     login_count += 1
#     username = input("请输入账号：")
#     password = input("请输入密码：")
#     if username == "admin" and password == "123456":
#         print("登录成功！")
#         break
#     else:
#         if login_count < 3:  # 1 2
#             print("登录失败！还有%d次机会" % (3 - login_count))
#         else:
#             print("账号已锁定！")


# 7.完成一个华氏度和摄氏度互相转换程序：首先提示用户输入温度，
# 然后询问用户输入的是华氏度还是摄氏度，转换算法如下：
# C表示摄氏度、F表示华氏度
# C = ( F - 32 ) / 1.8
# F = C * 1.8 + 32
# 输出保留小数点后两位
temp = float(input("请输入温度："))
temp_type = input("请问你输入的是华氏度（F）还是摄氏度（C）：")
if temp_type == "摄氏度" or temp_type == "C" or temp_type == "c":
    new_temp = temp * 1.8 + 32
    print("C%.3f ---> F%.2f" % (temp, new_temp))
elif temp_type == "华氏度" or temp_type == "F" or temp_type == "f":
    new_temp = (temp - 32) / 1.8
    print("F%.3f ---> C%.2f" % (temp, new_temp))
else:
    print("输入异常！")