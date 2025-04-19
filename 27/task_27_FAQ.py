""""""
"""
функция dist из библиотеки math, принимает в качестве входных данных два кортежа (x1, y1) и (x2, y2), 
а в качестве ответа возвращает расстояние между точками с данными координатами.
"""
from math import dist
p1 = (1,1)
p2 = (4,5)
s = dist(p1, p2)
print(s) # 5


# максимальное целое число, которое может быть представлено в Python
import sys
ma_n = sys.maxsize  # 9223372036854775807


# генератор вложенного цикла
a = 'abc'
d = '123'
for i in a:
    for k in d:
        print(k + i, end=' ')
print()
[print(k + i, end=' ') for i in a for k in d]
# 1a 2a 3a 1b 2b 3b 1c 2c 3c
# 1a 2a 3a 1b 2b 3b 1c 2c 3c
