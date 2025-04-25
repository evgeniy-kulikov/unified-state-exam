""""""
"""
Task 06
ЕГЭ Питоныч
https://stepik.org/course/100138
"""
# https://stepik.org/lesson/798013/step/4?unit=800901
from turtle import  *
# стартовые установки
tracer(0)
left(90)  # головой вдоль оси Y
k = 20  # коэфф. масштаба

# алгоритм
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
# формирование системы координат
penup()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot( )
done()  # отмена закрытия окна


""" 8.2 Решение задач. КУМИР """
# https://stepik.org/lesson/809558/step/2?unit=812807
from turtle import  *

tracer(0)
left(90)
k = 100
screensize(3000, 3000)
# алгоритм
for _ in range(10):
    forward(4 * k)
    right(60)
penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot('red') if x * y == 0 else dot()
done()
# 38


# https://stepik.org/lesson/809558/step/3?unit=812807
from turtle import  *
tracer(0)
left(90)
k = 80
screensize(2000, 2000)
for _ in range(10):
    forward(3 * k)
    right(45)
penup()
for x in range(-5, 10):
    for y in range(-5, 10):
        goto(x * k, y * k)
        dot('red') if not (x * y) else dot()
done()
# 44


# https://stepik.org/lesson/809558/step/5?unit=812807
from turtle import  *
tracer(0)
left(90)
k = 100
screensize(2000, 2000)
for _ in range(15):
    forward(2 * k)
    right(36)
penup()
for x in range(-5, 10):
    for y in range(-5, 10):
        goto(x * k, y * k)
        dot('red') if not (x * y) else dot()
done()
# 30


# https://stepik.org/lesson/809558/step/7?unit=812807
from turtle import  *
tracer(0)
left(90)
k = 40
screensize(3000, 3000)

for _ in range(2):
    forward(21 * k)
    right(90)
    forward(27 * k)
    right(90)

penup()
forward(9 * k)
right(90)
forward(10 * k)
left(90)

pendown()
for _ in range(2):
    forward(86 * k)
    right(90)
    forward(47 * k)
    right(90)

penup()
for x in range(-5, 80):
    for y in range(-5, 80):
        goto(x * k, y * k)
        dot('red') if not (x * y) else dot()
done()
# 234
