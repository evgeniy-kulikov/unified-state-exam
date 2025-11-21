""""""
"""
Task 09
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""

""" 7.15 ЕГЭ Тренировка 10 """

# https://stepik.org/lesson/444908/step/7?unit=435075
from re import *
reg = r'Милон\. |Милон \(.*\)\. '
with open('/add/course_57248/10-j7.txt', encoding='utf-8') as fl:
    f = fl.read()
    ls = findall(reg, f)
print(len(ls))  # 49  # принимается ответ 51 (похоже что ошибочно посчитали Милона в действующих лицах и еще где-то)
[print(i) for i in ls]


# https://stepik.org/lesson/444908/step/8?unit=435075
from re import *
reg = r'Олимп[ауоме]*'
with open('01_Demo/add/10-j7.txt', encoding='utf-8') as fl:
    f = fl.read()
    ls = findall(reg, f)
print(len(ls))  # 92 (нужно удалить сноску в начале текста)


# https://stepik.org/lesson/444908/step/9?unit=435075
from re import *
reg = r'В | в '
with open('01_Demo/add/10-j6.txt', encoding='utf-8') as fl:
    f = fl.read()
    ls = findall(reg, f)
print(len(ls))  # 29
