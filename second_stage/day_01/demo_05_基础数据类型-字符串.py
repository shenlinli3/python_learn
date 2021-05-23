# 字符串 str

# 字符串四种定义形式
# str_01 = "你好，世界！"
# str_02 = '你好，世界！'
# str_03 = '''你好，
# 世界！'''
# str_04 = """你好，世界！"""
# print(str_01, str_02, str_03, str_04)


# # 字符串转义
# str_05 = "I'm Bob"
# print(str_05)
# # 在python中原本有特殊含义的字符，在前面加上反斜杠之后，就会变成普通字符
# str_06 = 'I\'m Bob'
# print(str_06)
# str_07 = "这是反斜杠：\\"
# print(str_07)
# # 有一些字符，原本没有特殊含义，加上反斜杠之后，就会有
# # \n 换行符
# # \t 制表符
# print("你好\n世界")
# print("你好\t世界")


# # 字符串格式化
# # %d 格式化整型
# # %f 格式化浮点型
# # %s 格式化字符串
# s1 = "我是%s, 我喜欢%d个数字，分别是%d %.2f"
# print(s1 % ("zero", 2, 0, 9.9))
# print(s1 % ("zhangsan", 2, 100, 10.5))
# s2 = "我是%s 我喜欢%s"
# print(s2 % ("张三", "python"))
# print(s2 % ("lisi", "java"))


# 字符串的一些其它操作：
print(type("hello"))  # <class 'str'>
# 判断两个字符串是不是相等
print("hello" == "hello")
print("hello " == "hello")
# 函数 len() 可以用来判断字符串长度
print(len("hello world"))  # 11
# 字符串可以和字符串相加
print("hello" + " world")
# print("hello" + 10)
# 字符串可以和整型相乘
print("hello\n" * 3)

