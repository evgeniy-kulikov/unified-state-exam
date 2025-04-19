""""""
"""
№ 11 Информационный объём  Посимвольное кодирование
ЕГЭ Информатика
https://stepik.org/course/100056
"""


"""
from math import log2, ceil

print(log2(64))  # 6.0
print(log2(65))  # 6.022367813028454
print(ceil(log2(65)))  # 7  (ближайшее верхнее значение)
"""


# https://stepik.org/lesson/749257/step/4?unit=768530
from math import ceil, log2
k = 21
i = ceil(log2(7))
I = ceil(k * i / 8)
print(40 * I)


# https://stepik.org/lesson/749257/step/5?unit=768530
from math import ceil, log2
k = 11
N = 6
i = ceil(log2(N))  # 4
psw = ceil(k * i / 8)  # 5
res = psw * 20  # 100


# https://stepik.org/lesson/749257/step/6?unit=768530
from math import ceil, log2
k = 11
N = 10 + 12 + 12
i = ceil(log2(N))  # 6
psw = ceil(k * i / 8)  # 9  byte
res = psw * 60  # 540 byte


# https://stepik.org/lesson/749257/step/7?unit=768530
from math import ceil, log2
k = 15
N = 12
i = ceil(log2(N))  # 4
psw = ceil(k * i / 8) # 8  byte
res = (400 / 20) - psw  # 12 byte



# https://stepik.org/lesson/749257/step/9?unit=768530
from math import log2, ceil
k = 15
N = 12
i = ceil(log2(N) ) # 4
psw = ceil((i * k) / 8)  # 8
res = (300/ 20) - psw  # 7


# https://stepik.org/lesson/749257/step/11?unit=768530
from math import log2, ceil, floor
k = 9
N = 26 * 2 + 10  # 62
i = ceil(log2(N) ) # 6
psw = ceil((i * k) / 8)  # 7 byte
user = psw + 18  #  25 byte
res = floor(1024 / user)  # 40 byte


# https://stepik.org/lesson/749257/step/16?unit=768530
from math import log2, ceil
k = 6
N = 19 + 10  # 29
i = ceil(log2(N) ) # 5
car = ceil((i * k) / 8)  # 4 byte
res = ceil(car * 40)  # 160 byte


# https://stepik.org/lesson/749258/step/2?unit=768531
from math import log2, ceil
k = 252
N = 1700 + 10
i = ceil(log2(N)) # 11
user = ceil((i * k) / 8)  # 347 byte
res = ceil(user * 4096) / 1024 # 1388 kB


# https://stepik.org/lesson/749258/step/4?unit=768531
from math import log2, ceil
k = 250
N = 1650 + 10
i = ceil(log2(N)) # 11
user = ceil((i * k) / 8)  # 344 byte
res = ceil(user * 65536) / 1024 # 22016 kB


# https://stepik.org/lesson/749258/step/6?unit=768531
from math import log2, ceil
k = 11  # личный код
N = 10 + 26 * 2
i = ceil(log2(N)) # 6
# личный код + номер (в 1-м byte умещается десятичное число  255)
code_num = ceil((i * k) / 8) + 1  # 10
total = 28  # byte
add_info = total - code_num  # 18


# https://stepik.org/lesson/749258/step/10?unit=768531
from math import log2, ceil, floor
k1 = 10
N1 = 26
i1 = ceil(log2(N1))  # 5  bit
k2 = 5
N2 = 10
i2 = ceil(log2(N2))  # 4 bit
code = ceil((i1 * k1 + i2 * k2) / 8)  # 9 byte
add = 1800 / 40 - code  # 36  byte


# https://stepik.org/lesson/1397870/step/1?unit=1461022
from math import log2, ceil, floor
N = 10 + 52 + 458
i = ceil(log2(N))  # 10 bit
# single = floor((276 * 1024) / 862)  # 327 byte
# k = floor(8 * single / i)  # 261
single = 276 * 1024 // 862  # 327 byte  (Один серийный номер)
k = 8 * single // i  # 261
print(k)

N = 10 + 52 + 458
i = ceil(log2(N))  # 10 bit
for k in range(1, 1000):
    single = ceil(k * i / 8)  # Один серийный номер в байтах
    if single > 276 * 1024 // 862:
        print(k - 1)  # 261
        break


# https://stepik.org/lesson/1397870/step/3?unit=1461022
from math import log2, ceil
N = 10 + 52 + 68
i = ceil(log2(N))  # 8 bit
number = 287 * 1024 // 856  # 343 byte
k = number * 8 // i # 343
print(k)


# https://stepik.org/lesson/1397870/step/4?unit=1461022
from math import log2, ceil
N = 10 + 52 + 963
i = ceil(log2(N))  # 11 bit
number = 693 * 1024 // 2000  # 354 byte
k = number * 8 // i # 257
print(k)


# https://stepik.org/lesson/1397870/step/5?unit=1461022
from math import log2, ceil
k = 261
number = ceil(31 * 1024 ** 2 / 252_500)  # 129 byte
i = ceil(number * 8 / k)  # 4
N = 2 ** i  # 16
# мощность алфавита от 9 до 16. Минимальное из этого диапазона число 9
print(9)

# проверка
N = 9
i = ceil(log2(N))  # 4
number = ceil( i * k / 8)  # 131 byte
res = number * 252_500 / 1024 ** 2   # 31.545 MB  > 31 MB

# вариант
from math import log2, ceil
k = 261
for N in range(1, 1000):
    i = ceil(log2(N))  # i в битах
    number = ceil(k * i / 8)  # Один серийный номер в байтах
    if 252_500 * number > 31 * 1024 * 1024:
        print(N)
        break


# https://stepik.org/lesson/1397870/step/7?unit=1461022
from math import log2, ceil
k = 248
total = 16 * 1024 ** 2

for N in range(1, 1000):
    i = ceil(log2(N))  # bit
    I = ceil(i * k / 8)  # byte
    if  75_600 * I > total:
        print(N)   # 129
        break

# вариант
for i in range(2, 100):
    I = ceil(i * k / 8)  # один номер
    if 75_600 * I > total:
        print(2 ** (i - 1) + 1)  # 129
        break


# https://stepik.org/lesson/1397870/step/8?unit=1461022
from math import log2, ceil
k = 68
for N in range(2, 1000):
    i = ceil(log2(N))  # bit
    I = ceil(i * k / 8)  # byte
    if I * 680 > 16 * 1024:
        print(N)  # 5
        break


# https://stepik.org/lesson/1397870/step/9?unit=1461022
from math import ceil, log2
N = 10 + 26 + 8164
i = ceil(log2(N))
total = 156 * 1024
for k in range(1, 1000):
    if ceil(i * k / 8) * 835 > total:
        print(k)  # 110
        break


# https://stepik.org/lesson/1397870/step/9?unit=1461022
from math import ceil, log2
N = 10 + 26 + 450
i = ceil(log2(N))
total = 213 * 1024
for k in range(1, 1000):
    I = ceil(i * k / 8)
    if 708 * I > total:
        print(k)  # 274
        break


# https://stepik.org/lesson/1397870/step/3?unit=1461022
from math import ceil, log2
N = 10 + 52 + 68
i = ceil(log2(N))
total = 287 * 1024
for k in range(1, 1000):
    I = ceil(i * k / 8)
    if 856 * I >= total:  # не более
        print(k - 1)  # 343
        break


# https://stepik.org/lesson/1397870/step/5?unit=1461022
from math import ceil, log2
k = 261
total = 31 * 1024 ** 2
for N in range(2, 1000):
    i = ceil(log2(N))
    I = ceil(i * k / 8)
    if 252_500 * I > total:
        print(N)  # 9
        break


# https://stepik.org/lesson/1397870/step/7?unit=1461022
from math import ceil, log2
k = 248
total = 16 * 1024 ** 2
for N in range(2, 1000):
    i = ceil(log2(N))
    I = ceil(i * k / 8)
    if 75_600 * I > total:
        print(N)  # 129
        break

# https://stepik.org/lesson/749266/step/2?thread=solutions&unit=769628
from math import ceil, log2
k = 120_000
N = 4
i = ceil(log2(N))  # 2
I_new = ceil(k * i / 8) / 1024 # 29.296875 Kb
I_old = 1 * 120_000 / 1024
res = int(I_old - I_new)  # 87


# https://stepik.org/lesson/749266/step/3?unit=769628
from math import ceil, log2
k = 250
N = 100 + 4
i = ceil(log2(N))  # 7
I = ceil(k * i / 8)  # 219


# https://stepik.org/lesson/749266/step/5?&unit=769628
from math import log2 , ceil
# code
k_c = 5
N_c = 23 + 10
i_c = ceil(log2(N_c))
I_c = ceil(i_c * k_c / 8)  # 4 byte
# num
k_n = 1  # Номер кодируется не посимвольно, а сразу целиком.
N_n = 299 - 100 + 1  # 200
i_n = ceil(log2(N_n))  # 8 bit
I_n = ceil((i_n * k_n) / 8)  # 1 byte
total = 56  # byte
I_add = total - I_c - I_n  # 51 byte



# https://stepik.org/lesson/749266/step/6?&unit=769628
from math import log2 , ceil, trunc
# indif
k_i = 7 * 3
N_i = 16
i_i = ceil(log2(N_i))  # 4
I_c = ceil(i_i * k_i / 8)  # 11 byte

# bio
k_b = 10 * 3
N_b = 10
i_b = ceil(log2(N_b))  # 4
I_b = ceil(i_b * k_b / 8)  # 15 byte

total = 256
I_t = trunc((I_c + I_b) * total / 1024)  # 6



# https://stepik.org/lesson/619733/step/1?unit=1065192
from math import log2 , ceil
k = 30
N = 5
i = ceil(log2(N))  # 3
I = ceil(k * i / 8)  # 12
total = 50 * I  # 600


# https://stepik.org/lesson/619733/step/2?unit=1065192
from math import log2 , ceil
k = 40
N = 43
i = ceil(log2(N))  # 6
I = ceil(k * i / 8)  # 30



# https://stepik.org/lesson/619733/step/3?unit=1065192
from math import log2 , ceil
k = 6
N = 12 + 10
i = ceil(log2(N))  # 5
I = ceil(k * i / 8)  # 4
res = I * 32  # 128


# https://stepik.org/lesson/619733/step/4?unit=1065192
from math import log2 , ceil
k = 140
N = 43
i = ceil(log2(N))  # 6
I = ceil(k * i / 8)  # 105


# https://stepik.org/lesson/619733/step/5?unit=1065192
from math import log2 , ceil
k = 90
N = 197
i = ceil(log2(N))  # 8
I = ceil(k * i / 8)  # 90 kB


# https://stepik.org/lesson/619733/step/6?unit=1065192
from math import log2 , ceil
k = 25
N = 26
i = ceil(log2(N))  # 5
I = ceil(k * i / 8)  # 16 kB
total = I * 35  # 560 kB


# https://stepik.org/lesson/619733/step/7?unit=1065192
from math import log2 , ceil, trunc
k = 11
N = 10 + 32 * 2
i = ceil(log2(N))  # 7
I = ceil(i * k / 8)  # 10 byte
res = I * 50  # 500 byte


# https://stepik.org/lesson/619733/step/8?unit=1065192
from math import log2 , ceil
k = 315
I = 358 * 1024 // 1030
for N in range(1, 1000):
    i = ceil(log2(N))
    if ceil(i * k / 8) > I:
        print(N - 1)  # 512
        break


# https://stepik.org/lesson/619733/step/9?unit=1065192
from math import log2 , ceil
k = 10
N = 9
i = ceil(log2((N)))
I_psw = ceil(i * k / 8)  # 5 byte

total = 775 # byte
I = total / 25  # 31 byte
I_add = I - I_psw  # 26 byte
print(I_add * 8)  # 208 bit


# https://stepik.org/lesson/619733/step/10?unit=1065192
from math import log2
k = 1
N = 100
i = ceil(log2((N)))  # 7
I = i * k   # 7 bit
res = I * 80  # 560 bit


