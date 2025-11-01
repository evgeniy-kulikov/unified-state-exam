""""""
"""
Task 17
Подборка задач для подготовки к ЕГЭ по информатике 2026 | itpy
https://stepik.org/course/122969
"""

""" 1.4 Повторение 4 часть """
# https://stepik.org/lesson/1343760/step/1?unit=1359470
cnt = 0
MX = 0
with open('add/course_122969/17_1.txt') as file:
    d = list(map(int, file))
    mn = min(i for i in d if not i % 19)
    for i in range(len(d) - 1):
        if any(k for k in d[i:i+2] if not k % mn):
            cnt += 1
            MX = max(MX, sum(d[i:i+2]))
    print(cnt, MX)  # 142 175430


# https://stepik.org/lesson/1343760/step/2?unit=1359470
cnt = 0
MX = 0
with open('add/course_122969/17_2.txt') as file:
    d = list(map(int, file))
    mn = max(i for i in d if abs(i) % 10 == 3 and len(str(abs(i))) == 5)
    for i in range(len(d) - 2):
        if any(k for k in d[i:i+3] if str(k)[-1] == '3'):
            if sum(d[i:i+3]) <= mn:
                cnt += 1
                MX = max(MX, sum(d[i:i+3]))
    print(cnt, MX)  # 1767 99081



""" 4.7 Проверочная: Работа с файлами, номера: 9, 17, 24 """
# https://stepik.org/lesson/1231755/step/5?unit=1245338
with open('add/course_122969/17_4_7_01.txt') as file:
    cnt = 0
    MX = 0
    d = list(map(int, file))
    MN = min(i for i in d if 10**2 <= i < 10**3 and i % 10 == 3)
    for i in range(len(d) - 1):
        a, b = d[i:i+2]
        if sum(1 for i in [a,b] if 10**3 <= i < 10**4) == 1:
            if not (a**2 + b**2) % MN:
                cnt += 1
                MX = max(MX, a**2 + b**2)
    print(cnt, MX)  # 74 433966217 Пишется слитно


# https://stepik.org/lesson/1231755/step/6?unit=1245338
with open('add/course_122969/17_4_7_02.txt') as file:
    cnt = 0
    res = 0
    d = list(map(int, file))
    MX = max(i for i in d if 10**2 <= abs(i) < 10**3 and abs(i) % 10 == 3)
    for i in range(len(d) - 2):
        ls = d[i:i+3]
        if sum(1 for i in ls if 10**2 <= abs(i) < 10**3 and abs(i) % 10 == 3):
            if sum(ls) < MX:
                cnt += 1
                res = max(res, sum(ls))
    print(cnt, res)  # 147 944 Пишется слитно


# https://stepik.org/lesson/1231755/step/6?unit=1245338
"""
Для решения этой задачи необходимо найти минимальный чётный элемент в последовательности, затем пройти по всем последовательным тройкам элементов (a, b, c) и проверить, соответствуют ли они условиям: 
- среди пар (a, c) один элемент чётный, другой — нечётный
- средний элемент (b) кратен минимальному чётному элементу последовательности. 
После этого подсчитывается количество таких троек и находится пара (a, c) с минимальной суммой.
"""
with open('add/course_122969/17_4_7_03.txt') as file:
    cnt = 0
    res = 10**6
    d = list(map(int, file))
    MN = min(i for i in d if not i % 2)
    for i in range(len(d) - 2):
        a, b, c = d[i:i+3]
        num = [i for i in [a, c] if not i % 2]
        if len(num) == 1 and not b % MN:
            cnt += 1
            res = min(res, a + c)
    print(cnt, res)  # 159 1261 Пишется слитно






