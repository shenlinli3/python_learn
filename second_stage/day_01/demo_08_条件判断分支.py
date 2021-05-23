# input() 输入函数
# 该函数接收到的任何内容都是字符串类型

# in1 = input("请输入账号：")
# in2 = input("请输入密码：")
# print(in1, in2)


# 条件判断分支
# if 如果
# elif 又如果
# else 否则


# num1 = int(input("请输入第一个数："))
# num2 = int(input("请输入第二个数："))
# if num1 > num2:  # True False
#     print("第一个数大于第二个数")
#     print("Test...1")
# elif num1 < num2:
#     print("第一个数小于第二个数")
#     print("Test...2")
# else:
#     print("第一个数等于第二个数")
#     print("Test...3")
# print("End...")


# weather = input("今天天气怎么样：")
# if weather == "晴天":
#     sun = input("太阳大不大？")
#     if sun == "大":
#         print("穿短裤 戴墨镜")
#     else:
#         print("记得吃雪糕")
# elif weather == "雨天":
#     print("带把伞")
# elif weather == "雪天":
#     print("打雪仗记得带头盔")
# elif weather == "多云":
#     print("在家打游戏")
# else:
#     print("我听不懂你在说什么")


# 写一个小程序，用户输入0-100分，程序输出非常优秀（91-100）、
# 优秀（81-90）、良好（71-80）、及格（60-70）、不及格（0-59）等评级
score = float(input("请输入分数："))
if 100 >= score >= 91:
    print("非常优秀")
elif 91 > score >= 81:
    print("优秀")
elif 81 > score >= 71:
    print("良好")
elif 71 > score >= 60:
    print("及格")
elif 60 > score >= 0:
    print("不及格")
else:
    print("分数异常")
