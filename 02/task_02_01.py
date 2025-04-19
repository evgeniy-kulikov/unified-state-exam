"""
Task 02
Информатика Подготовка к ЕГЭ 2025
https://stepik.org/course/182932/syllabus
"""

# https://stepik.org/lesson/1341300/step/1?thread=solutions&unit=1356964
print(*'xzyw')
for x in [0, 1]:
    for y in [0, 1]:
        for w in [0, 1]:
            for z in [0, 1]:
                if all([x or not y, y != z, not w]):
                    print(x, y, z, w)
# x z y w
# 0 0 1 0
# 1 0 1 0
# 1 1 0 0

from itertools import product
print(*'xzyw')
# for x, z, y, w in product((0, 1), (0, 1), (0, 1), (0, 1)):
for x, z, y, w in product((0, 1), repeat=4):
    if all([x or not y, y != z, not w]):
        print(x, y, z, w)
# x z y w
# 0 0 1 0
# 1 1 0 0
# 1 0 1 0


# https://stepik.org/lesson/1084605/step/1?unit=1094967
from itertools import product
print(*'xwzy')
for x, z, y, w in product((0, 1), repeat=4):
    if all([x or not y, y != z, w]):
        print(x, w, z, y)
# x w z y       y w z x
# 0 1 1 0       0 1 1 0
# 1 1 1 0       0 1 1 0
# 1 1 0 1       1 1 0 1



# https://stepik.org/lesson/1084605/step/2?thread=solutions&unit=1094967
from itertools import product
print(*'abc')
for a, b, c in product((0, 1), repeat=3):
    if (a and not c) or (not b and not c):
        print(a, b, c, ' F=1')
    elif (not a or c) and (b or c):
        print(a, b, c, ' F=0')
# a b c
# 0 0 0  F=1
# 0 0 1  F=0
# 0 1 0  F=0
# 0 1 1  F=0
# 1 0 0  F=1
# 1 0 1  F=0
# 1 1 0  F=1
# 1 1 1  F=0


# https://stepik.org/lesson/1084605/step/4?unit=1094967
from itertools import product
print(*'yzwx')
for x, y, w, z in product((0, 1), repeat=4):
    if ((not x and y) == z) and w:
        print(y, z, w, x)
# y z w x
# 1 0 1 1
# 1 1 1 0
# 0 0 1 0
# 0 0 1 1


# https://stepik.org/lesson/1084605/step/5?thread=solutions&unit=1094967
from itertools import product
print(*'ywxz')
for y, w, x, z in product((0, 1), repeat=4):
    # if all([(x and not y or z), not w]):
    if all([(x > y or z), not w]):
        print(y, w, x, z)
# y w x z
# 0 0 1 0
# 0 0 1 1
# 1 0 1 1
# 0 0 0 1
# 1 0 0 1


# https://stepik.org/lesson/1084605/step/6?thread=solutions&unit=1094967
from itertools import product
print(*'ywzx')
for y, w, x, z in product((0, 1), repeat=4):
    if not any([x and not y, x == z, w]):
    # if all([y or not x, x != z, not w]):
        print(y, w, z, x)
# y w z x
# 1 0 0 1
# 0 0 1 0
# 1 0 1 0
# верные варианты ywzx  ywxz


# https://stepik.org/lesson/1084605/step/7?thread=solutions&unit=1094967
from itertools import product
print(*'zwyx')
for z, w, y, x in product((0, 1), repeat=4):
    if not all([y <= (x or z), z <= y]):
    # if any([y > (x and z), z > y]):
        print(z, w, y, x)
# z w y x
# 1 0 0 0
# 1 1 0 0
# 1 0 0 1
# 0 0 1 0   # 0 1 1 0


# https://stepik.org/lesson/1084605/step/12?thread=solutions&unit=1094967
from itertools import product
print(*'wzyx')
for w, z, y, x in product((0, 1), repeat=4):
    if all([not w, (y or z) <= (not x and y)]):
        print(w, z, y, x)
# w z y x
# 0 0 0 1
# 0 0 1 0
# 0 1 1 0


# https://stepik.org/lesson/1084605/step/16?thread=solutions&unit=1094967
from itertools import product
print(*'zxwy')
for z, x, w, y in product((0, 1), repeat=4):
    if not ((not z or w) or ((z <= w) == (x <= y))):
        print(z, x, w, y)
# z x w y
# 1 0 0 0
# 1 1 0 1
# 1 0 0 1