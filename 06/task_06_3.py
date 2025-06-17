""""""
"""
Task 06
https://stepik.org/course/100056
ЕГЭ Информатика
"""

""" 15.1 Решаем вариантик """
# https://stepik.org/lesson/766574/step/5?unit=768992
from turtle import *
tracer(0)
lt(90)
k = 50
screensize(2000, 2000)
rt(90)
for _ in range(3):
    rt(45)
    fd(10*k)
    rt(45)
rt(315)
fd(10*k)
for _ in range(2):
    rt(90)
    fd(10 * k)

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot('red') if not x*y else dot()
done()
# 203