# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/19 17:00
@Author  : zero
"""

# 输入一个列表，并计算该列表的各个范围区间，按照指定格式输出
# 假设现在输入这样一个列表：[0, 2, 3, 4, 6, 7, 9, 123, 124, 125, 126]
# 说明：如上，列表中0和下一个2不是连续数字，2 3 4是连续的，6 7是连续的，123~126是连续的
# 要求输出：['0', '2->4', '6->7', '9', '123->126']
nums = [0, 2, 3, 4, 6, 7, 9, 123, 124, 125, 126, 3]
final_nums = []  # [[0], [2, 3, 4], [6, 7]]
temp_nums = []  # []
for index, i in enumerate(nums):
    temp_nums.append(i)
    print(temp_nums)
    if index == len(nums) - 1:
        final_nums.append(temp_nums)
        break
    if temp_nums[-1] + 1 != nums[index + 1]:
        final_nums.append(temp_nums)
        temp_nums = []
print(final_nums)
print([f"{i[0]}->{i[-1]}" if len(i) > 1 else str(i[0]) for i in final_nums])

