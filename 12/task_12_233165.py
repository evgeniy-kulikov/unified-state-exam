""""""
"""
Task 12
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 12.1 Задание 12 | Урок 1 """
# https://stepik.org/lesson/1695399/step/3?unit=1718750
#  https://kompege.ru/task  № 24174 (Уровень: Базовый)
# пусть n0 = кол-ву нулей, а n2 = кол-ву двоек => n1 = 2 * n2 (кол-ву единиц)
for n0 in range(1000):
    for n2 in range(1000):
        str1 = '0' * n0 + '1' * 2 * n2 + '2' * n2  # формируем нашу строку
        if len(str1) == 1000:  # проверяем, что строка имеет именно 1000 символов
            sum1 = sum(map(int, str1))
            str2 = str1.replace('1', '+')  # защита от наложения замен друг на друга
            str2 = str2.replace('2', '1').replace('0', '2').replace('+', '0')
            sum2 = sum(map(int, str2))
            if sum2 == sum1 + 1640:
                print(str1.count('0'))  # 880

# variant
for n2 in range(1, 1001):
    n1 = 2 * n2
    n0 = 1000 - n1 - n2
    sum1 = n1 + 2 * n2
    sum2 = 2 * n0 + n2
    if sum1 == sum2 - 1640:
        print(n0)


# https://stepik.org/lesson/1695399/step/4?unit=1718750
#  https://kompege.ru/task  № 24173 (Уровень: Базовый)
for n0 in range(1, 1000):
    for n1 in range(1, 501):
        s = '0' * n0 + '1' * n1 + '2' * n1
        if len(s) == 1000:
            sm1 = sum(map(int, s))
            s = s.replace('0', 'z').replace('1', '*')
            s = s.replace('2', '1').replace('z', '2').replace('*', '0')
            sm2 = sum(map(int, s))
            if sm1 - sm2 == 178:
                print(s.count('1'))  # 363

# variant
for n2 in range(1, 501):
    sm1 = 3 * n2
    sm2 = (1000 - 2 * n2) * 2 + n2
    a = sm1 - sm2
    if sm1 - sm2 == 178:
        print(n2)  # 363


# https://stepik.org/lesson/1695399/step/5?unit=1718750
#  https://kompege.ru/task  № 23847 (Уровень: Базовый)
s = '1' * 400 + '2' * 250 + '3' * 360
# '1'-->'3' + '2'-->'3'
print(400 + 250)  # 650


# https://stepik.org/lesson/1695399/step/6?unit=1718750
#  https://kompege.ru/task  № 23846 (Уровень: Базовый)
# s = 'x' * 512 + 'y' * 200 + 'z' * 288
print(200 + 1)


# https://stepik.org/lesson/1695399/step/7?unit=1718750
#  https://kompege.ru/task  № 23727 (Уровень: Базовый)
# s1 = '0' * 250 + '1' * 750
# s2 = '1' * 750 + '0' * 250
print(250)


# https://stepik.org/lesson/1695399/step/8?unit=1718750
#  https://kompege.ru/task  № 24176 (Уровень: Средний)
"""
X, R, q1  - эта команда означает, что при считывании единицы в ячейку записывается цифра «X» из набора [0, 1, 2], 
но записывается она постоянно при всем проходе по ленте головки влево.  
Т.е. нужно рассмотреть все три случая записи цифры «X»
"""
for n in range(1, 501):  # n - кол-во нулей и единиц
    sum1 = n + 2 * (1000 - 2 * n)
    for x in range(3):  # перебор числа Х
        s1 = '2' * n + str(x) * n + '1' * (1000 - 2 * n)  # программа q1
        # программа q2
        s2 = s1.replace('0', '*').replace('1', '+')  # защита от наложения замен
        s2 = s2.replace('2', '0').replace('*', '1').replace('+', '2')
        sum2 = sum(map(int, s2))
        if sum1 == sum2 + 363:
            print(s2.count(str(x)))  # 274

# Решение без работы со строкой, но сложное для понимания. Уж лучше строки
for n in range(1, 501):  # n - кол. 0 и 1
    n2 = (1000 - 2 * n)  # n2 - кол. 2
    sum1 = n + 2*n2
    for x in range(3):  # перебор числа Х
        sum2 = (n + 2*n2, 2*n + 2*n2, 2*n2)[x]
        if sum1 == sum2 + 363:
            print((n, n, n2)[x])  # 274


# https://stepik.org/lesson/1695399/step/9?unit=1718750
#  https://kompege.ru/task  № 23750 Демоверсия 2026 (Уровень: Средний)
print(999)  # 999


# https://stepik.org/lesson/1695399/step/10?unit=1718750
#  https://kompege.ru/task  № 23859 (Уровень: Базовый)
for n in range(1, 501):
    sm1 = n + 2 * (1000 - 2 * n)
    sm2 = n + 2 * n
    if sm1 == sm2 + 200:
        print(1000 - 2 * n)  # 400


# https://stepik.org/lesson/1695399/step/11?unit=1718750
#  https://kompege.ru/task  № 23858 (Уровень: Базовый)
for n in range(1, 501):
    sm = 3*n
    if sm == 432:
        print(n)  # 144


# https://stepik.org/lesson/1695399/step/12?unit=1718750
#  https://kompege.ru/task  № 23851 (Уровень: Базовый)
s = [*'1' * 750 + '0' * 650 + '2']
q = 0
for i in range(len(s)):
    if not q:
        if s[i] == '0':
            s[i] = '1'
            q = 1
        elif s[i] == '1':
            s[i] = '0'
            q = 1
        else:
            s[i] = '1'
            break
    else:
        if s[i] == '0':
            s[i] = '1'
            q = 0
        elif s[i] == '1':
            s[i] = '0'
            q = 0
        else:
            s[i] = '0'
            break
print(s.count('1'))



""" 12.2 Задание 12 | Задачи прошлых лет """
# https://stepik.org/lesson/1695402/step/1?unit=1718753
#  https://kompege.ru/task  № 23750 Демоверсия 2026 (Уровень: Средний)
print(999)  # 999






""""""
""" Варианты """
# 29.1 Вариант 2 | Часть 1
# https://stepik.org/lesson/1729865/step/13?unit=1753692
for n in range(4, 10_000):
    s = '1' + '2' * n
    while '12' in s or '322' in s or '222' in s:
        s = s.replace('12', '2', 1)
        s = s.replace('322', '21', 1)
        s = s.replace('222', '3', 1)
    if sum(map(int, s)) == 15:
        print(n)  # 37
        break


# 31.1 Вариант 4 | Часть 1
# https://stepik.org/lesson/1736669/step/13?unit=1760675
for n in range(3, 10_000):
    s = '3' + '1' * n
    while '31' in s or '211' in s or '1111' in s:
        s = s.replace('31', '1', 1)
        s = s.replace('211', '13', 1)
        s = s.replace('1111', '2', 1)
    if sum([*map(int, s)]) == 15:
        print(n)  # 50
        break


# 32.1 Вариант 5 | Часть 1
# https://stepik.org/lesson/1754188/step/13?unit=1778647
for n in range(4, 10_000):
    s = '4' + '2' * n
    while '42' in s or '8222' in s or '2222' in s:
        s = s.replace('42', '2', 1)
        s = s.replace('8222', '24', 1)
        s = s.replace('2222', '8', 1)
    if sum(map(int, s)) == 110:
        print(n)  # 1591
        break


# 33.1 Вариант 6 | Часть 1
# https://stepik.org/lesson/1943170/step/12?unit=1969924
# https://kompege.ru/task  № 23195 Основная волна 10.06.25 (Уровень: Базовый)
for n in range(4, 10_000):
    s = '7' + '8' * n
    while '78' in s or '688' in s or '8888' in s:
        s = s.replace('78', '8', 1)
        s = s.replace('688', '87', 1)
        s = s.replace('8888', '6', 1)
    if sum(map(int, s)) == 61:
        print(n)  # 348
        break


# 34.1 Вариант 7 | Часть 1
# https://stepik.org/lesson/1943172/step/13?unit=1969926
res = 0
for n in range(4, 4000):
    s = '1' + '2' * n
    while '12' in s or '322' in s or '2222' in s:
        s = s.replace('12', '2', 1)
        s = s.replace('322', '21', 1)
        s = s.replace('2222', '3', 1)
    res = max(res, sum(map(int, s)))
print(res)  # 89


# 35.1 Вариант 8 | Часть 1
# https://stepik.org/lesson/1943178/step/13?unit=1969932
sm = 0
for n in range(4, 10_000):
    s = '4' + '2' * n
    while '42' in s or '822' in s or '222' in s:
        s = s.replace('42', '2', 1)
        s = s.replace('822', '24', 1)
        s = s.replace('222', '8', 1)
    sm = max(sm, sum(map(int, s)))
print(sm)  # 40


