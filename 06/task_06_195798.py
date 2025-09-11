""""""
"""
Task 06
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""


""" 10.2 Практика (ур. базовый) """
# # https://stepik.org/lesson/1220762/step/1?unit=12341554155
from turtle import *
tracer(0)
lt(90)
k = 40
screensize(2000, 2000)

rt(45)
for _ in range(7):
    fd(k*6)
    rt(45)
    fd(k*12)
    rt(135)

pu()
for x in range(-3,23):
    for y in range(-3, 23):
        goto(x*k, y*k)
        dot('red') if not x*y else dot()
done()  # 44


# https://stepik.org/lesson/1220762/step/3?unit=12341554155
from turtle import *
tracer(0)
lt(90)
screensize(2000, 2000)
k = 30
for _ in range(2):
    fd(24*k)
    rt(90)
    fd(16*k)
    rt(90)
pu()
fd(10*k)
rt(90)
fd(8*k)
lt(90)
pd()
for _ in range(2):
    fd(15*k)
    rt(90)
    fd(28*k)
    rt(90)
pu()
for x in range(-5, 50):
    for y in range(-5, 30):
        goto(x*k, y*k)
        dot('red') if not x*y else dot()
done()  #91


# https://stepik.org/lesson/1220762/step/4?unit=1234155
from turtle import *
tracer(0)
lt(90)
screensize(2000, 2000)
k = 20
for _ in range(2):
    fd(10*k)
    rt(90)
    fd(20*k)
    rt(90)
pu()
fd(3*k)
rt(90)
fd(7*k)
lt(90)
pd()
for _ in range(2):
    fd(70*k)
    rt(90)
    fd(90*k)
    rt(90)
pu()
for x in range(-5, 90):
    for y in range(-5, 90):
        goto(x*k, y*k)
        dot('red') if not x*y else dot()
done()  # 112


# https://stepik.org/lesson/1220762/step/5?unit=1234155
from turtle import *
tracer(0)
lt(90)
screensize(2000, 2000)
k = 40
for _ in range(7):
    fd(20*k)
    rt(240)
    fd(10*k)
    rt(240)
    fd(20 * k)
    rt(120)
    fd(10 * k)
    rt(120)
pu()
for x in range(-10, 20):
    for y in range(-5, 25):
        goto(x*k, y*k)
        dot('red') if not x*y else dot()
done()  # 38 * 2 = 76




""" 10.3 Практика (ур. усложненный) """
# https://stepik.org/lesson/1220763/step/2?unit=1234156
from turtle import *

tracer(0)
lt(90)
screensize(2000, 2000)
k = 30
for _ in range(9):
    fd(18*k)
    lt(72)
pu()
for x in range(-50, 5):
    for y in range(-10, 50):
        goto(x*k, y*k)
        dot('red') if not x*y else dot()
done() # fd(18) == 18


# https://stepik.org/lesson/1220763/step/2?unit=1234156
from turtle import *
tracer(0)
lt(90)
screensize(2000, 2000)
k = 30
for _ in range(8):
    for i in range(4):
        fd(5*k)
        rt(30)
        fd(6*k)
        rt(150)
    rt(60)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot('red') if not x*y else dot()
done() # (3 * 5) * 6 = 90


# https://stepik.org/lesson/1220763/step/5?unit=1234156
from turtle import *
tracer(0)
lt(90)
screensize(2000, 2000)
k = 50

for _ in range(6):
    for i in range(3):
        fd(7*k)
        rt(120)
    rt(60)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot('red') if not x*y else dot()
done()  # (18 * 4) + 24 * 2 = 120


# https://stepik.org/lesson/1220763/step/6?unit=1234156
from turtle import *
tracer(0)
lt(90)
k = 2
for _ in range(9):
    fd(65*k)
    lt(45)
    fd(100*k)
    lt(65)
    fd(65)
    lt(90)
done()  # 9

