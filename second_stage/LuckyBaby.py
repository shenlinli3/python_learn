# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/18 16:07
@Author  : zero
"""
# 游戏规则：生死有命，富贵在天！

import time
import random

names = ["邵浩", "赵斌", "郑伟杰", "伸林", "刘英男", "陈剑云",
         "李博越", "郭耀旗", "余钢", "许邦", "范金鹏", "孙佳旺",
         "李峰", "肖方正", "毛万喜", "李娇娇", "姜功喜", "唐志聪",
         "王晨", "严帅", "吴小发"]

for i in range(3):
    print(f"\r抽奖倒计时！{3 - i}秒", end="")
    time.sleep(1)
sample_count = random.randint(15, 18)
lucky_babies = random.sample(names, sample_count)

print("\r公布抽奖结果：")
for index, i in enumerate(lucky_babies, start=1):
    print(f"第{index}个幸运观众：{i}")
    time.sleep(0.5)

print(lucky_babies)

# 保留第一次抽奖结果
# ['姜功喜', '王晨', '郑伟杰', '邵浩', '李娇娇', '李博越', '唐志聪', '范金鹏', '伸林', '孙佳旺', '李峰', '郭耀旗', '许邦', '陈剑云', '刘英男', '严帅']
