""" https://kompege.ru/task """
"""
10713 17630
"""


# 10713 (Уровень: Средний)
from math import ceil
r = ceil((4 * 4 + 3 * 3) / 8) * 500
print(r)  # 2000

# 17630 Основная волна 19.06.24 (Уровень: Средний)
from math import log2, ceil
for n in range(1, 1000):
    if ceil(n * ceil(log2(10 + 26 + 450)) / 8) * 708 > 213 * 1024:
        print(n)  # 274
        break