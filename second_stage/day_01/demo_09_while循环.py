# 循环

# while 当

# 1~10000
# count_num = 1
# while count_num < 10001:  # 条件表达式为真时进入循环
#     print(count_num)  # 0~9
#     count_num += 1
# print("循环结束了")

# 100~1
# start_num = 100
# while start_num > 0:
#     print(start_num)
#     start_num -= 1

# 求出1~100所有数的和
# start_num = 1
# sums = 0
# while start_num <= 100:
#     # print(start_num)
#     sums += start_num
#     start_num += 1
# print(sums)


# 循环中两个关键字 break continue

# # break 打破、破坏
# start_num = 1
# while start_num <= 100:
#     print(start_num)
#     if start_num == 77:
#         break
#     start_num += 1
# print("循环结束了")

# # continue 继续
# start_num = 1
# while start_num <= 100:
#     if start_num == 77:
#         start_num += 1
#         continue
#     print(start_num)
#     start_num += 1


# 循环中的else
n = 1
while n <= 10:
    print(n)
    if n == 7:
        break
    n += 1
else:
    # 当n不再满足<=10的时候
    print("循环正常结束了")