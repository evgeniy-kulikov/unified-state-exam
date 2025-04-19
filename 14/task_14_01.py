"""
Task 14
Информатика Подготовка к ЕГЭ 2025
https://stepik.org/course/182932
Задачи с поиском числа в другой СС
"""

# https://stepik.org/lesson/1084606/step/1?unit=1094968
n_10 = 64 ** 30 + 2 ** 300 - 4
n_8 = oct(n_10)
print(n_8.count('7'))


# https://stepik.org/lesson/1084606/step/2?unit=1094968
from string import digits, ascii_uppercase
def convert(num, base):
    '''
    Получение числа в другой системе счисления
    :param num: int
    :param base: int
    :return: str
    '''
    alfa = digits + ascii_uppercase
    res = ''
    while num:
        res = alfa[num % base] + res
        num //= base
    return res
num = 3 * 16 ** 8 - 4 ** 5 + 3
res = convert(num, 4)
print(res)
print(res.count('3'))
# 23333333333300003
# 12


# https://stepik.org/lesson/1084606/step/3?unit=1094968
from string import digits, ascii_uppercase
def convert(num, base):
    alfa = digits + ascii_uppercase
    res = ''
    while num:
        res = alfa[num % base] + res
        num //= base
    return res
num = 2 * 27 ** 7 + 3 ** 10 - 9
res = convert(num, 3)
print(res.count('0'))  # 13


# https://stepik.org/lesson/1084606/step/4?unit=1094968
def convert_10(num, base):
    res = ''
    while num:
        res = str(num % base) + res
        num //= base
    return res
num = 51 * 7 ** 12 - 7 ** 3 - 22
res = convert_10(num, 7)
print(sum(map(int, res)))  # 70


"""
Преобразование числа в десятичную СС
"""

# https://stepik.org/lesson/1084607/step/1?thread=solutions&unit=1094969
for n in '0123456789ABCDE':
    res = int(f'123{n}5', 15) + int(f'1{n}233', 15)
    if res % 14 == 0:
        # print(n) # 4
        print(res / 14)  # 8767
        break


# https://stepik.org/lesson/1084607/step/2?thread=solutions&unit=1094969
for n in '0123456789ABCDEFG':
    res = int(f'9759{n}', 17) + int(f'3{n}108', 17)
    if res % 11 == 0:
        print(n) # 2
        print(res / 11)  # 95306
        break


# https://stepik.org/lesson/1084607/step/3?thread=solutions&unit=1094969
# Обернул циклы в функцию, что бы сразу выйти из всех вышестоящих циклов.
def get_num():
    alfa = '0123456789ABCD'
    for n_14 in alfa:
        for n_12 in alfa[:12]:
            for n_11 in alfa[:11]:
                if int(f'3364{n_11}', 11) + int(f'{n_12}7946', 12) == int(f'55{n_14}87', 14):
                    # print(n_11, n_12, n_14)  # 7 7 7
                    return (int(f'55{n_14}87', 14))

print(get_num())  # 207291

# немного хуже
for n_14 in '0123456789ABCD':
    for n_12 in '0123456789AB':
        for n_11 in '0123456789A':
            if int(f'3364{n_11}', 11) + int(f'{n_12}7946', 12) == int(f'55{n_14}87', 14):
                # print(n_11, n_12, n_14)  # 7 7 7
                print(int(f'55{n_14}87', 14))  # 207291
                break


# https://stepik.org/lesson/1084607/step/4?thread=solutions&unit=1094969
for y in '0123456789ABCDEFG':
    for x in '0123456789ABCDE':
        res = int(f'123{x}5', 15) + int(f'67{y}9', 17)
        if res % 131 == 0:
            print(f'{res / 131},  x={x},  y={y}')
# 686.0,  x=B,  y=8
# 685.0,  x=0,  y=A
# 686


# https://stepik.org/lesson/1084607/step/5?unit=1094969
from string import digits, ascii_uppercase
alfa = digits + ascii_uppercase[:11]

for x in alfa:
    cnt = 0
    for y in alfa:
        res = int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)
        if res % 18 == 0:
            cnt += 1
            # print(f'x={x},  y={y}')
    if cnt == 21:
        print(x) # 3
        print((int(f'125{x}9', 21) + int(f'36599', 21)) / 18)  # 47594
        break


# https://stepik.org/lesson/1084607/step/6?unit=1094969
for x in range(68):
    a = 5 + x * 68 + 3 * 68 ** 2 + 2 * 68 ** 3 + 68 ** 4
    b = 3 + 3 * 68 + 2 * 68 ** 2 + x * 68 ** 3 + 68 ** 4
    res = a + b
    if (res) % 12 == 0:
        print(res // 12, x)  # 5321454 65
