# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/12 10:05
@Author  : zero
"""

# 字符串是不可变数据类型，所有对字符串的操作，都是复制一份新的

# 1. str.upper()  字符串转大写
str01 = "Hello World!"
print(str01.upper())
print(str01)

# 2. str.lower()  字符串转小写
print("Hello World!".lower())

# 3. str.isupper()  判断字符串是否全部大写
print("Hello".isupper())
print("HELLO".isupper())

# 4. str.islower()  判断字符串是否全部小写
print("hello".islower())
print("Hello".islower())

# 5. str.startswith()  判断字符串是否以指定子串开头
print("Hello World".startswith("hello"))
print("Hello World".startswith("H"))
print(" Hello World".startswith("Hello "))

# 6. str.endswith()  判断字符串是否以指定子串结尾
print("Hello World".endswith("World"))
print("Hello World".endswith(" World"))
print("Hello World".endswith(" World "))

# 7. str.index()  返回指定子串在字符串中的索引位
print("Hello World".index("Wor"))
# print("Hello World".index("wor"))  # 找不到则报错
print("Hello World".index("Wor", 2))

# 8. str.count()  返回指定子串在字符串中出现的次数
print("Hello World".count("l"))
print("Hello World".count("lo"))

# 9. str.find()  返回指定子串在字符串中的索引位
print("Hello World".find("Wor"))
print("Hello World".find("wor"))  # 找不到则返回-1

# 10. str.rfind()  返回指定子串在字符串中的索引位，从右边开始查找
print("Hello World".rfind("l"))  # 9

# 11. str.capitalize()  字符串首字母转大写
print("hello".capitalize())

# 12. str.strip()  默认去除字符串前后的 空格符、制表符、换行符
print(" he l lo\t\n".strip())
print("hello")
print("$#%$hello^$".strip("$#^"))
# 13. str.lstrip()  同上，只去除左边
# 14. str.rstrip()  同上，只去除右边

# 15. str.split()  根据指定子串切割字符串，默认根据空格切割，得到的结果是一个列表
print("hello world python".split())
print("https://www.baidu.com".split("."))
print("https://www.baidu.com".split("/"))
print("https://www.baidu.com".split("//"))

# 16. str.replace()  使用指定子串替换指定子串
print("hello".replace("l", "r"))
print("hello".replace("l", "r", 1))

# 17. str.isascii()  判断一个字符串是否在ascii编码中
print("hello123!@#$% ".isascii())
print("hello123!@#$% 你好".isascii())

# 18. str.isdigit()  判断一个字符串是否全部是数字
print("12345".isdigit())
print("12345.".isdigit())
print("12345.5".isdigit())
print("12345你好".isdigit())

# 19. str.isalpha()  判断一个字符串是否全是英文字母
print("helloWORLD".isalpha())
print("helloWORLD1".isalpha())
print("helloWORLD中文".isalpha() and "helloWORLD中文".isascii())

# 20. str.isalnum()  判断一个字符串是否全是英文字母或数字
print("helloWORLD1".isalnum())
print("helloWORLD1 ".isalnum())
print("helloWORLD1你哈".isalnum())

# 21. str.encode()  把字符串按照指定的格式编码为字节
print("abc你好".encode(encoding="utf-8"))  # b'abc\xe4\xbd\xa0\xe5\xa5\xbd'

# 22. str.join()  把可迭代对象中的字符串以当前字符串为分割符拼起来
print(" ".join(["Hello", "World", "Hello", "Python"]))
print("$".join("hello"))

# 23. str.format()  格式化字符串
name01 = "zhangsan"
name02 = "lisi"
hobby01 = "python"
hobby02 = "java"
print("%s like %s %s like %s" % (name01, hobby01, name02, hobby02))
print("{} like {} {} like {}".format(name01, hobby01, name02, hobby02))
print("{0} like {1} {2} like {1}".format(name01, hobby01, name02))
print("{n1} like {h1} {n2} like {h1}".format(n1=name01, h1=hobby01, n2=name02))