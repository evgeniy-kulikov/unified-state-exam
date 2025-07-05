""""""
"""
Task 06
https://stepik.org/course/57248
Подготовка к ЕГЭ информатика
"""

""" 7.10 ЕГЭ Тренировка 6 """

# https://stepik.org/lesson/421030/step/3?auth=login&unit=410640
from turtle import  *
tracer(0)
lt(90)
k = 50
for _ in range(15):
    fd(k * 4)
    rt(60)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x*k, y*k)
        dot('red') if not x*y else dot()
done()  # 28


# https://stepik.org/lesson/421030/step/4?auth=login&unit=410640
from turtle import *
tracer(0)
lt(90)
k = 100
screensize(2000, 2000)
for _ in range(10):
    rt(60)
    fd(10 * k)
    rt(60)
penup()
for x in range(-1, 10):
    for y in range(-10, 10):
        goto(x*k, y*k)
        dot('red') if not x*y else dot()
done()  # 42


# https://stepik.org/lesson/421030/step/5?auth=login&unit=410640
from turtle import *
tracer(0)
lt(90)
k = 50
screensize(3000, 2000)
for _ in range(8):
    fd(12 * k)
    rt(90)
pu()
for x in range(-1, 15):
    for y in range(-1, 15):
        goto(x*k, y*k)
        dot('red') if not x*y else dot()
done()  #  11*11 = 121


# https://stepik.org/lesson/421030/step/6?auth=login&unit=410640
from turtle import *
tracer(0)
lt(90)
k = 100
screensize(2000, 2000)
for _ in range(36):
    rt(60)
    fd(1*k)
    rt(60)
    fd(1*k)
    rt(270)
pu()
for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x*k, y*k)
        dot('red') if not x*y else dot()
done()  #  6 * 4 = 24

