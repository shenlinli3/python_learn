# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/22 16:55
@Author  : zero
"""

# # 1.
# class Student:
#     def __init__(self, name, score):
#         if not (isinstance(name, str) and isinstance(score, (int, float))):
#             raise ValueError("Student.name must be 'str' type. Student.score must be 'int' or 'float' type")
#         self.name = name
#         self.score = score
#
# s1 = Student("小明", 99)
# s1.score = "A"
# print(s1.score)


# 2.
# class Student:
#     def __init__(self, name, score):
#         if not (isinstance(name, str) and isinstance(score, (int, float))):
#             raise ValueError("Student.name must be 'str' type. "
#                              "Student.score must be 'int' or 'float' type")
#         self.__name = name
#         self.__score = score
#
#     def get_score(self):
#         return self.__score
#
#     def set_score(self, new_score):
#         if not isinstance(new_score, (int, float)):
#             raise ValueError("Student.score must be 'int' or 'float' type")
#         self.__score = new_score
#
# s1 = Student("小明", 99)
# s1.set_score(100)
# print(s1.get_score())


# 3.
class Student:
    def __init__(self, name, score):
        if not (isinstance(name, str) and isinstance(score, (int, float))):
            raise ValueError("Student().name must be 'str' type. "
                             "Student().score must be 'int' or 'float' type")
        self.__name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        if not isinstance(new_score, (int, float)):
            raise ValueError("Student().score must be 'int' or 'float' type")
        self.__score = new_score

s1 = Student("小明", 99)
print(s1.score)
s1.score = 100
s1.score = "A"
print(s1.score)
