# 数字型 number
    # int 整型
    # float 浮点型
    # complex 复数
    # bool 布尔
        # True
        # False

# num_01 = 10
# num_02 = -10
# num_03 = 10.5
# # 怎么判断一个对象的类型呢？ type()
# print(type(num_01))  # <class 'int'>
# print(type(num_02))  # <class 'int'>
# print(type(num_03))  # <class 'float'>


# # 算术运算符 七种
# # 加
# print(10 + 10)  # 20
# # 减
# print(10 - 5)  # 5
# # 乘
# print(10 * 10)  # 100
# # 除
# print(10 / 10)  # 1.0
# # 整除
# print(10 // 10)  # 1
# print(7 // 2)  # 3
# # 次幂
# print(10 ** 3)  # 1000
# # 取余
# print(7 % 2)  # 1
# print(10 % 4)  # 2


# # 随堂练习：假设现有任意一个三位整型 100 153 234 ... 999
# # 要求求出它们的百位、十位、个位上的数字
# num01 = 657
# print(num01 // 100)
# # print(num01 // 10 % 10)
# print(num01 % 100 // 10)
# print(num01 % 10)


# # 比较运算符
# # 大于
# print(10 > 5)  # True
# # 小于
# print(5 < 3)  # False
# # 等于
# print(5 == 5)  # True
# # 不等于  在旧版本中可以写成 <>
# print(5 != 5)  # False
# # 大于等于
# print(10 >= 10)
# print(10 >= 9)
# # 小于等于
# print(5 <= 5)
# print(5 <= 6)


# 赋值运算符
# 先执行等号右边，再把运算的值赋予给左边
a = 10
# 加等于
a += 20  # a = a + 20
print(a)  # 30
# 减等于
a -= 10
print(a)  # 20
# 乘等于
a *= 5
print(a)  # 100
# 除等于
a /= 10
print(a)  # 10.0
# 整除等于
a //= 1
print(a)  # 10.0  # 整除任意一边是浮点型，则得到的结果也是浮点型
# 次幂等于
a **= 3
print(a)
# 取余等于
a %= 999
print(a)
