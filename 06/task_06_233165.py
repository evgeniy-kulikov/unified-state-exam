""""""
"""
Task 05
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 6.1 Задание 6 | Урок 1 """
# https://stepik.org/lesson/1650991/step/11?unit=1673693
# 06/pic/course_233165/001.gif
# https://kompege.ru/task   № 12882 (Уровень: Базовый)
from turtle import *
tracer(0)
lt(90)
k = 50
screensize(2000, 2000)

lt(255)
for _ in range(3):
    lt(30)
    for __ in range(4):
        fd(10*k)
        lt(90)
pu()
for x in range(-50, 50):
    for y in range(0, 50):
        goto(x*k, y*k)
        dot()
done()


# 34.1 Вариант 7 | Часть 1
# https://stepik.org/lesson/1943172/step/6?unit=1969926
# https://kompege.ru/task  № 23265 Основная волна 11.06.25 (Уровень: Базовый)
print(21*13 + 14*7 - 12*6)  # 299
# exit()
from turtle import *
tracer(0)
screensize(4000,4000)
lt(90)
k = 30
for _ in range(2):
    fd(20*k)
    lt(270)
    fd(12*k)
    rt(90)
pu()
fd(9*k)
rt(90)
fd(7*k)
lt(90)
pd()
for _ in range(2):
    fd(13*k)
    rt(90)
    fd(6*k)
    rt(90)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x*k, y*k)
        dot(3, 'red')
done()
