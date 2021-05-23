# 快捷键 Ctrl + d 快速的往下复制一行

# 等号：先执行右边，再执行左边，把等号右边的值赋予给左边
# a就是变量名
a = "你好，新世界！"

print(a)
print(a)
print(a)
print(a)
print(a)


# 变量的命名规则
# python中的变量应该以英文数字下划线组成，不能以数字开头
# 不能和python中的关键字重名，比如print
# 多个单词用下划线隔开
# 尽量做到见名知意

day_01 = "01"
birthday_of_boy = "xxx"  # python推荐使用这种写法
birthdayOfBoy = "xxx"  # 驼峰式

# 1day 数字开头 不行
# print_a 可以
# num_01 可以
# _num 可以
# @num 不可以


# 程序其实就是数据或状态的变化
hp = 650
print(hp)
hp = hp + 50
print(hp)

s = 10
s + 10
s = 20  # 20
s = s + 10
print(s)  # 30