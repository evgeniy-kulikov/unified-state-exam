""""""
"""
Task 05
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 5.1 Задание 5 | Урок 1 """
# https://stepik.org/lesson/1650989/step/3?unit=1673691
for n in range(1, 1000):
    r = f'{n:b}'
    r += ('0', '1')[r.count('1') % 2]
    # r += ('0', '1')[r.count('1') % 2]
    r += str(r.count('1') % 2)
    r = int(r, 2)
    if r > 130:
        print(r)  # 132
        break


# https://stepik.org/lesson/1650989/step/4?unit=1673691
# https://kompege.ru/task   № 558 (Уровень: Базовый)
for n in range(1, 1000):
    r = f'{n:b}'
    r += r[-1]
    r += str(r.count('1') % 2)
    r += str(r.count('1') % 2)
    r = int(r, 2)
    if r > 97:
        print(n)  # 13
        break


# https://stepik.org/lesson/1650989/step/5?unit=1673691
# https://kompege.ru/task   № 1513 (Уровень: Средний)
for n in range(1, 1000):
    r = f'{n:b}'
    r += r[-1]
    r += '01'[r.count('1') % 2]
    r += str(r.count('1') % 2)
    if int(r, 2) > 90:
        print(n)  # 11
        break


# https://stepik.org/lesson/1650989/step/6?unit=1673691
# https://kompege.ru/task   № ***
res = set()
for n in range(1, 1000):
    r = f'{n:b}'
    r += str(r.count('1') % 2)
    r += str(r.count('1') % 2)  # r += '0'  всегда будет '0'
    r = (int(r, 2))
    if 210 <= r <= 260:
        res.add(r)
print(len(res))  # 14


# https://stepik.org/lesson/1650989/step/7?unit=1673691
# https://kompege.ru/task   № 2230 (Уровень: Базовый)
res = 0
for n in range(1, 100):
    b = f'{n:b}'
    if n % 2:
        b = '1' + b + '11'
    else:
        b = '11' + b + '00'
    r = int(b, 2)
    if r < 127:
        res = max(res, r)
print(res)  # 120


# https://stepik.org/lesson/1650989/step/8?unit=1673691
# https://kompege.ru/task   № 5358 Новогодний вариант 2022/23 (Уровень: Средний)
for n in range(6, 1000):
    b = f'{n:b}'
    if b[:3].count('1') % 2:
        b = '10' + b[2:] + '1'
    else:
        b = '1' + b[:-2] + '01'
    if int(b, 2) > 50:
        print(n)  # 20
        break


# https://stepik.org/lesson/1650989/step/8?unit=1673691
# https://kompege.ru/task   № 5358 Новогодний вариант 2022/23 (Уровень: Средний)
for n in range(6, 1000):
    b = f'{n:b}'
    if b[:3].count('1') % 2:
        b = '10' + b[2:] + '1'
    else:
        b = '1' + b[:-2] + '01'
    if int(b, 2) > 50:
        print(n)  # 20
        break


# https://stepik.org/lesson/1650989/step/9?unit=1673691
# https://kompege.ru/task   № 6884 OpenFIPI (Уровень: Базовый)
MN = 10**6
for n in range(1,1000):
    b = f'{n:b}'
    if n % 2:
        b = '11' + b + '11'
    else:
        b = '1' + b + '0'
    r = int(b, 2)
    if r > 225:
        MN = min(MN, r)
print(MN)  # 228


# https://stepik.org/lesson/1650989/step/10?unit=1673691
# https://kompege.ru/task   № 6885 OpenFIPI (Уровень: Базовый)
MN = 10**6
res = []
for n in range(4,1000):
    b = f'{n:b}'
    if n % 2:
        b += f'{b.count("1"):b}'
    else:
        b = '1' + b + '00'
    r = int(b, 2)
    if r > 190:
        MN = min(MN, r)
        res.append((MN, n))
print(min(res)[1])  # 16

# risk
for n in range(4,1000):
    b = f'{n:b}'
    if n % 2:
        b += f'{b.count("1"):b}'
    else:
        b = '1' + b + '00'
    r = int(b, 2)
    if r > 190:
        print(n)  # 16
        break




""" 5.2 Задание 5 | Урок 2 """
# https://stepik.org/lesson/1659948/step/1?unit=1682802
# https://kompege.ru/task   № 49 Джобс 31.08.2020 (Уровень: Базовый)
for n in range(1, 1000):
    r = f'{n:b}'
    r += str(r.count('1') % 2)
    r += str(r.count('1') % 2)
    r = int(r, 2)
    if r > 80:
        print(r)  # 86
        break


# https://stepik.org/lesson/1659948/step/2?unit=1682802
# https://kompege.ru/task   № 405 (Уровень: Базовый)
for n in range(1, 1000):
    r = f'{n:b}'
    # r += ('01', '10')[int(r[-1])]
    r += ('01', '10')[n % 2]
    r = int(r, 2)
    if r > 81:
        print(r)  # 86
        break


# https://stepik.org/lesson/1659948/step/3?unit=1682802
# https://kompege.ru/task   № 549 (Уровень: Базовый)
for n in range(1, 1000):
    r = f'{n:b}'
    r += r[-1]
    r += str(r.count('1') % 2)
    r += str(r.count('1') % 2)
    if int(r, 2) > 130:
        print(n)  # 17
        break


# https://stepik.org/lesson/1659948/step/5?unit=1682802
# https://kompege.ru/task   № 561 (Уровень: Средний)
def cv(n):
    r = ''
    while n:
        r += str(n % 3)
        n //= 3
    return r[::-1]

for n in range(1, 1000):
    r = cv(n)
    r += str(n % 3)
    r = int(r, 3)
    if r >= 100:
        print(r)  # 103
        break



""" 5.3 Задание 5 | Урок 3 """
# https://stepik.org/lesson/1667484/step/1?unit=1690472
# https://kompege.ru/task   № 9828 Основная волна 27.06.23 (Уровень: Средний)
def cv(n):
    r = ''
    while n:
        r += str(n % 3)
        n //= 3
    return r[::-1]

for n in range(1000, 0, -1):
    r = cv(n)
    if n % 3:
        r += cv(n % 3 * 4)
    else:
        r = '1' + r + '02'
    if int(r, 3) < 199:
        print(n)  # 20
        break



""" 5.4 Задание 5 | Задачи прошлых лет """
# https://stepik.org/lesson/1650990/step/1?unit=1673692
# https://kompege.ru/task   № 9736 Основная волна 19.06.23 (Уровень: Базовый)
res = 0
for n in range(100):
    r = f'{n:b}'
    if n % 3:
        r += f'{n % 3 * 3:b}'
    else:
        r += r[-3:]
    r = int(r, 2)
    if r <= 170:
        res = max(res, r)
print(res)  # 166

