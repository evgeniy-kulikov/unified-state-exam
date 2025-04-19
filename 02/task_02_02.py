"""
Task 02
https://stepik.org/course/57248
Подготовка к ЕГЭ информатика
"""

# https://stepik.org/lesson/257025/step/1?unit=237402
def fn(a):
    for t in range(1, 1000):  # целых положительных t
        for m in range(1, 1000):  # целых положительных m
            f1 = 3 * t + 8 * m > 89
            f2 = m < a and t <= a
            if not (f1 or f2):
                return False
    return True

for a in range(-1000, 1000):
    if fn(a):
        print(a)  # 27
        break


# https://stepik.org/lesson/257025/step/2?unit=237402
def fn(a):
    for x in range(1000):  # целых неотрицательных  x
        for y in range(1000):  # целых неотрицательных  y
            f1 = 2 * x + 3 * y != 72
            f2 =a > x and a > y
            if not (f1 or f2):
                return False
    return True

for a in range(-1000, 1000):
    if fn(a):
        print(a)  # 37
        break


# https://stepik.org/lesson/257025/step/3?unit=237402
def fn(a):
    for x in range(1, 1000):  # целых положительных   x
        for y in range(1, 1000):  # целых положительных   y
            f1 = 6 * x + 4 * y != 34
            f2 = a > 5 * x + 3 * y
            f3 = a > 4 * y + 15 * x - 35
            if not (f1 or f2 and f3):
                return False
    return True

for a in range(-1000, 1000):
    if fn(a):
        print(a)  # 45
        break


# https://stepik.org/lesson/257025/step/4?unit=237402
def fn(a):
    for x in range(1, 1000):  # целых положительных   x
        for y in range(1, 1000):  # целых положительных   y
            f1 = y - x ** 2 != 80
            f2 = a < 13 * x - 14
            f3 = a < y ** 2 + 15
            if not (f1 or f2 or f3):
                return False
    return True

for a in range(6570, 7000):  # внимание на f1 и f3
    if fn(a):
        print(a)  # 6575
        # break


# https://stepik.org/lesson/257639/step/1?unit=238073
# 02/pic/pic_02_001.jpg
from  itertools import product
print(*'wzyx')
for w, z, y, x in product((0, 1), repeat=4):
    f1 = x and not y
    f2 = y == z
    f3 = not w
    if not (f1 or f2 or f3):
        print(w, z, y, x)
# w z y x
# 1 0 1 0
# 1 0 1 1
# 1 1 0 0


# https://stepik.org/lesson/257639/step/2?unit=238073
from  itertools import product
print(*'ywzx')
for y, w, z, x in product((1, 0), repeat=4):
    # f1 = not x or y  # варианты
    # f2 = not y or w
    # f3 = z == (x or y)
    # if not (f1 and f2 or f3):

    # if not ((not x or y) and (not y or w) or (z == (x or y))):  # варианты
    # if not (x <= y and y <= w or (z == (x or y))):  # варианты
    if (x > y or y > w) and z != (x or y):  # варианты
        print(y, w, z, x)
# y w z x
# 1 0 0 1
# 1 0 0 0
# 0 1 0 1
# 0 0 0 1

# Новый метод решения  !!!
def func(x, y, z, w):
   return ((x <= y) and (y <= w)) or (z == (x or y))

print(*'ywzx')
for i in range(2 ** 4):  #  4 - кол-во переменных
    x = bin(i)[2:].zfill(4)
    lst = list(map(int, x))
    if not func(*lst):
        print(*lst)
# y w z x
# 0 1 0 0
# 1 0 0 0
# 1 0 0 1
# 1 1 0 0


# Новый метод решения  !!!
# https://stepik.org/lesson/257639/step/3?unit=238073
print(*'yxwz')
for i in range(2 ** 4):  #  4 - кол-во переменных
    b = bin(i)[2:].zfill(4)
    y, x, w, z = map(int, b)
    if not (x and not y or (y == z) or w):
        print(y, x, w, z)
# y x w z
# 0 0 0 1
# 1 0 0 0
# 1 1 0 0


# https://stepik.org/lesson/257645/step/2?unit=238081
print(*'yxwz')
for i in range(16):
    b = bin(i)[2:].zfill(4)
    y,x,w,z = map(int, b)
    if not ((x and not y) or (y == z) or w):
        print(y,x,w,z)
# y x w z
# 0 0 0 1
# 1 0 0 0
# 1 1 0 0


# https://stepik.org/lesson/257645/step/3?unit=238081
print(*'zyxw')
for i in range(16):
    b = bin(i)[2:].zfill(4)
    z,y,x,w = map(int, b)
    if not (((x <= y) == (z <= w)) or x * w):
        print(z,y,x,w)
# z y x w
# 1 0 0 0
# 1 1 0 0
# 1 1 1 0


# https://stepik.org/lesson/421642/step/1?unit=411296
print(*'wyzx')
for i in range(2 ** 4):
    b = bin(i)[2:].zfill(4)
    w, y, z, x = map(int, b)
    if not (((y or w) <= (x <= z)) <= (x <= w)):
        print(w, y, z, x)
# w y z x
# 0 0 0 1
# 0 0 1 1
# 0 1 1 1


# https://stepik.org/lesson/421642/step/2?unit=411296
print(*'yzxw')
for i in range(2 ** 4):
    y, z, x, w = map(int, bin(i)[2:].zfill(4))
    f = (x == (not y)) <= ((x and w) == z)
    if not (f):
        print(y, z, x, w)
# y z x w
# 1 1 0 0
# 1 1 0 1
# 0 1 1 0
# 0 0 1 1

# https://stepik.org/lesson/421642/step/3?unit=411296
from itertools import product
print(*'yzwx')
for y,z,w,x in product((0,1), repeat=4):
    if ((not x and y) == z) and w:
        print(y,z,w,x)
# y z w x
# 1 0 1 1
# 1 1 1 0
# 0 0 1 0
# 0 0 1 1

# https://stepik.org/lesson/421642/step/4?unit=411296
from itertools import product
print(*'yzxw')
for y,z,x,w in product((0,1), repeat=4):
    if not (any([x, z and not w, y and not w, y and not z])):
        print(y,z,x,w)
# y z x w
# 0 0 0 0
# 0 0 0 1
# 0 1 0 1
# 1 1 0 1

# https://stepik.org/lesson/421642/step/5?unit=411296
print(*'yzwx')
for i in range(2 ** 4):
    y,z,w,x = map(int, bin(i)[2:].zfill(4))
    if not (((x <= z) and (z <= w)) or (y == (x or z))):
        print(y,z,w,x)
# y z w x
# 0 1 0 0
# 0 0 1 1
# 0 1 0 1
# 0 0 0 1

# https://stepik.org/lesson/421642/step/5?unit=411296
print(*'cab')
for i in range(2 ** 3):
    c,a,b = map(int, bin(i)[2:].zfill(3))
    # if (a and not c) or (not a and b and c):
    if not ((a and not c) or (not a and b and c)):
        print(c,a,b)
# c a b
# F=1
# 0 1 0
# 0 1 1
# 1 0 1
# F=0
# 0 0 0
# 0 0 1
# 1 0 0
# 1 1 0
# 1 1 1


