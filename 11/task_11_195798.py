""""""
"""
Task 11
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""


""" 16.2 Практика (ур. базовый) """
# https://stepik.org/lesson/1223081/step/1?unit=1236570
from math import log2, ceil
I = ceil(310 * ceil(log2(10 + 2042)) / 8) + 14
print(I * 65_536 / 2**10)  # 30656


# https://stepik.org/lesson/1223081/step/5?unit=1236570
from math import log2, ceil
psw = ceil(25 * ceil(log2(7)) / 8)
# (psw + add) * 200 = 4800
add = 4800 / 200 - psw
print(add)  # 14


# https://stepik.org/lesson/1223081/step/7?unit=1236570
from math import log2, ceil
ind = ceil(70 * ceil(log2(10 + 1015)) / 8)
psw = ceil(20 * ceil(log2(10 + 1015)) / 8)
total = (ind + psw) * 32768 / 2**10
print(total)  # 4000


# https://stepik.org/lesson/1223081/step/8?unit=1236570
from math import log2, ceil
psw = ceil(11 * ceil(log2(12)) / 8)
# (psw + add) * 50 = 700
add = 700 / 50 - psw
print(add)  # 8


# https://stepik.org/lesson/1223081/step/9?unit=1236570
from math import log2, ceil
ind = ceil(1024 * ceil(log2(10 + 300)) / 8)
print(131_072 * ind / 2**20)  # 144


# https://stepik.org/lesson/1223081/step/10?unit=1236570
from math import log2, ceil
i = ceil(log2(10_000))  # 14
print(68 * i)  # 952


# https://stepik.org/lesson/1223081/step/11?unit=1236570
from math import log2, ceil
ind = ceil(110 * ceil(log2(10 + 1020)) / 8)
print(32_768 * ind / 2 **10)  # 4864


# https://stepik.org/lesson/1223081/step/12?unit=1236570
from math import log2, ceil
psw = ceil(16 * ceil(log2(26 * 2 + 10)) / 8)
add = 20
print((10 * 2**10 / (psw + add)))  # 320


# https://stepik.org/lesson/1223081/step/13?unit=1236570
from math import log2, ceil
psw = ceil(35 * ceil(log2(4090 + 10)) / 8)
# (psw + add) * 300 = 96000
add = 96000 / 300 - psw
print(add)  # 263


# https://stepik.org/lesson/1223081/step/14?unit=1236570
from math import log2, ceil
psw = ceil(17 * ceil(log2(19 + 2)) / 8)
add = 485
print((psw + add) * 4096 / 2**10)  # 1984


# https://stepik.org/lesson/1223081/step/15?unit=1236570
from math import log2, ceil
ind = ceil(60 * ceil(log2(10 + 250)) / 8)
print(ind * 65_536 / 2**10)  # 4352



""" 16.3 Практика (ур. усложненный) """

# https://stepik.org/lesson/1223082/step/1?unit=1236571
from math import log2, ceil
id_1 = 15 * ceil(log2(26))
id_2 = 4 * ceil(log2(10))
full = ceil((id_1 + id_2) / 8) + 12
print(1600 // full)  # 66


# https://stepik.org/lesson/1223082/step/2?unit=1236571
from math import log2, ceil
num = ceil((ceil(log2(10_000))) / 8)  # все число а не 5 разрядов
fio = ceil(80 * ceil(log2(33 * 2 + 2)) / 8)
psw = ceil(20 * ceil(log2(26 + 7)) / 8)
print(25 * (num + fio + psw))  # 2175


# https://stepik.org/lesson/1223082/step/3?unit=1236571
from math import log2, ceil
ru = ceil((ceil(log2(10 + 33*2))) * 20_000 / 8)
en = ceil((ceil(log2(10 + 26*2))) * 20_000 / 8)
print(ru - en)  # 2500



""" 16.4 Закрепление """
# https://stepik.org/lesson/1223083/step/11?unit=1236572
from math import log2, ceil
# code + num + add
code = ceil(17 * ceil(log2(26*2 + 10 + 9)) / 8)
num = ceil(ceil(log2(1200)) / 8)
print(48 - (code + num))  # 31


