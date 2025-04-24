"""
Task 02
https://stepik.org/course/100138
ЕГЭ Питоныч
"""

# https://stepik.org/lesson/559878/step/2?unit=553923
from itertools import product
print(*'xyzf')
for x, y, z in product((0 , 1), repeat=3):
    f = (z and not y) or not x
    print(x, y, z, int(f))

# вариант
print(*'xyzf')
for i in range(2**3):
    b = f'{i:b}'.zfill(3)
    x, y, z = map(int, b)
    f = (z and not y) or not x
    print(x, y, z, int(f))
# x y z f
# 0 0 0 1
# 0 0 1 1
# 0 1 0 1
# 0 1 1 1
# 1 0 0 0
# 1 0 1 1
# 1 1 0 0
# 1 1 1 0

# https://stepik.org/lesson/559878/step/3?unit=553923
print(*'xyzf')
for i in range(2**3):
    b = f'{i:b}'.zfill(3)
    x, y, z = map(int, b)
    f = x and z or x and not y
    print(x, y, z, int(f))


# https://stepik.org/lesson/559878/step/11?unit=553923
from itertools import product
print(*'xyzwf')
for x, y, z, w in product((0, 1), repeat=4):
    f = (z <= y) and ((x <= w) == (y <= x))
    print(x, y, z, w, int(f))


""" 15.4 Решение задания 2 КЕГЭ """
# https://stepik.org/lesson/568559/step/2?unit=562974
from itertools import product
print(*'xyzf')
for x, y, z in product((0, 1), repeat=3):
    f = (z and not y) or not x
    print(x, y, z, int(f))
# yxz


# https://stepik.org/lesson/568559/step/4?unit=562974
print(*'xyzf')
for i in range(2**3):
    b = f'{i:b}'.zfill(3)
    x, y, z = map(int, b)
    f = (x and z) or (x and not y)
    print(x, y, z, int(f))
# yzxf


""" 15.5 Решение задания 2 КЕГЭ. Часть 2 """
# https://stepik.org/lesson/576913/step/2?unit=571524
print(*'abcdf')
for i in range(2 ** 4):
    b = f'{i:b}'.zfill(4)
    a, b, c, d = map(int, b)
    f = (not a and not b) or (b == c) or d
    if not f:
        print(a, b, c, d, int(f))
# cdba

# https://stepik.org/lesson/576913/step/4?unit=571524
from itertools import product
print(*'y,x,z,f'.split(','))
for y,x,z in product([0, 1], repeat=3):
    f = ((y or x) <= z) or (x == z)
    if not f:
        print(y,x,z,0)


""" 15.6 Решение задания 2 КЕГЭ. Часть 3 """
# https://stepik.org/lesson/1400834/step/2?unit=1417790
from itertools import product
print(*'wxyz')
for w, x, y, z in product((0, 1), repeat=4):
    f = not (x <= w) or (y <= z) or not y
    if not f:
        print(w, x, y, z)
# yxwz


# https://stepik.org/lesson/1400834/step/3?unit=1417790
print(*'x, z, y, w'.split(', '))
for i in range(16):
    x, z, y, w = map(int, f'{i:b}'.zfill(4))
    f = (y <= (not (x <= z))) or w
    if not f:
        print(x, z, y, w)
# xzyw


# https://stepik.org/lesson/1400834/step/4?unit=1417790
print(*'z, x, y, w'.split(', '))
for i in range(16):
    z, x, y, w = map(int, f'{i:b}'.zfill(4))
    f = (not (x <= z)) or (y == w) or y
    if not f:
        print(z, x, y, w)
# zxyw
