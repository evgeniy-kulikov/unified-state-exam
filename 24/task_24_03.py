"""
Task 24
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""

""" 7.37 ЕГЭ Тренировка 24 """
from re import *
reg = r'C+'
with open('add/course_57248/k7-0.txt') as fl:
    ls = findall(reg, fl.read())
    if ls: print(len(max(ls, key=len)))
    else: print(0)  # 0
# В файле k7-0.txt нет символов  C

