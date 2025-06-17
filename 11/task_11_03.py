""""""
"""
Task 11
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""


""" 7.16 ЕГЭ Тренировка 11 """

# https://stepik.org/lesson/444909/step/1?auth=login&unit=435076
from math import log2, ceil
I = ceil(15 * ceil(log2(9)) / 8 ) * 25
print(I) # 200

# https://stepik.org/lesson/444909/step/2?auth=login&unit=435076
from math import log2, ceil
I = ceil(ceil(log2(6)) * 11 / 8) * 20
print(I)  # 100


# https://stepik.org/lesson/444909/step/4?auth=login&unit=435076
from math import log2, ceil
I = (ceil(ceil(log2(10)) * 9 / 8) + 6) * 100
print(I)  # 1100


# https://stepik.org/lesson/444909/step/7?auth=login&unit=435076
# !!! Интересная задача !!!
"""
Фишка с этажами: 
используем не три разряда с десяти символьным алфавитом, 
а один разряд, но с 199 символьным алфавитом (получается экономия в 1 байт)
"""
from math import log2, ceil
I_code = ceil(ceil(log2(33)) * 5 / 8)  # 4
I_floor = ceil(ceil(log2(199)) / 8)  # 1
print(56 - I_code - I_floor)  # 51


# https://stepik.org/lesson/444909/step/8?auth=login&unit=435076
from math import log2, ceil
I_user = ceil(ceil(log2(36)) * 14 / 8)  # 11
I_group = ceil((ceil(log2(6)) * 5 + ceil(log2(10) * 3))  / 8) # 4
print(30 - I_group - I_user)  # 15


# https://stepik.org/lesson/444909/step/9?auth=login&unit=435076
from math import log2, ceil
I_1 = ceil(log2(26)) * 15  # 75 bit
I_2 = ceil(log2(10)) * 8  # 32 bit
I_code = ceil((I_1 + I_2) / 8) # 14 byte
I_add = 3150 / 35 - I_code
print(I_add)  # 76 byte


# https://stepik.org/lesson/444909/step/10?unit=435076
from math import log2, ceil
I_psw = ceil(15 * ceil(log2(10 + 52)) / 8)  # 12 byte
print(700/20 - I_psw)  # 23 byte



""" 7.17 ЕГЭ Тренировка 11 """

# https://stepik.org/lesson/648384/step/1?auth=login&unit=645015
from math import log2, ceil
I_1 = ceil(log2(26)) * 15  # 75 bit
I_2 = ceil(log2(9999))  # 14 bit
I_id = ceil((I_1 + I_2) / 8) # 12 byte
res = int(1600 / (I_id + 12))
print(res)  # 66 user


# https://stepik.org/lesson/648384/step/2?auth=login&unit=6450156
from math import log2, ceil
I_one = 10 * ceil(log2(26))  # 50 bit
I_two = log2(99999)  # 16.6092 bit
# I_two2 = (5 * log2(10))  # 16.6094 bit
I_1 = ceil((I_one + I_two) / 8)  # 9 byte
print((1800 // (I_1 + 13)))  #  81 user


