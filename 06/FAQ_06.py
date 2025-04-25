from turtle import  *

# вперед
forward(int/float)
fd(int/float)

# назад
backward(int/float)
bk(int/float)
back(int/float)

# поворот направо
right(int/float)
rt(int/float)

# поворот налево
left(int/float)
lt(int/float)


# В Python черепаха по умолчанию направлена вдоль оси X, а в Кумире вдоль оси Y
# По этому нужно всегда повернуть черепаху налево.
left(90)

# переместить в точку
goto(int/float, int/float)
setpos(int/float, int/float)

# установка координаты
setx(int/float)
sety(int/float)

# получить текущую координату
xcor(int/float)
ycor(int/float)

# поднять / опустить перо
penup()
pu()
up()

pendown()  # по умолчанию перо всегда опущено
pd()
down()

# точка с размером
dot(int)

# размер экрана (высота / ширина)
screensize(int, int)

# включение / отключение анимации черепахи
tracer(0)

# отмена закрытия окна
done()

"""
Стандартный вид программы
"""
from turtle import  *
# стартовые установки
tracer(0)
left(90)  # головой вверх, вдоль оси Y
k = 100  # коэфф. масштаба  (расстояние между точками в пикселях)
screensize(3000, 3000)  # размер окна (с прокруткой)

# алгоритм
for _ in range(10):
    forward(4 * k)
    right(60)

# формирование системы координат
penup()
for x in range(-10, 10):  #  играемся значениями
    for y in range(-10, 10):  #  играемся значениями
        goto(x * k, y * k)
        # точки на осях - красные
        dot('red') if x * y == 0 else dot('grey')

done()  # отмена закрытия окна
