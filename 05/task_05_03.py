""""""
"""
Task 05
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

""" 32.1 Обработка чисел в двоичном представлении. Часть 1 """
# https://stepik.org/lesson/770696/step/3?unit=773131
with open('05.txt') as fl:
    for f in fl:
        f = f.strip()
        b = bin(int(f))[2:] + '0'
        n = int(b, 2)
        if f == '30':
            print(f'{f} --> {n}')  # 60
        else:
            print(n)


# https://stepik.org/lesson/770696/step/4?unit=773131
for i in range(11, 21):
    b = bin(i)[2:] + '1'
    n = int(b, 2)
    if i == 20:
        print(f'{i} --> {n}')  # 41
    else:
        print(n)


# https://stepik.org/lesson/770696/step/5?unit=773131
for i in range(1, 41):
    b = '1' + bin(i)[2:] + '0'
    n = int(b, 2)
    if n > 70:
        print(n)  # 96
        break


# https://stepik.org/lesson/770696/step/7?unit=773131
cnt = 0
for i in range(9):
    b = bin(i)[2:]
    cnt += b.count('1') == 1
print(cnt)  # 4


# https://stepik.org/lesson/770696/step/8?unit=773131
cnt = 0
for i in range(10, 100):
    b = bin(i)[2:]
    cnt += b.count('0') == 4
print(cnt)  # 18


# https://stepik.org/lesson/770696/step/9?unit=773131
for i in range(100, 1000):
    b = bin(i)[2:]
    if b.count('1') == 5:
        print(i)  # 103
        break


# https://stepik.org/lesson/770696/step/13?unit=773131
for i in range(1, 100):
    b = bin(i)[2:]
    b += str(sum(map(int, b)) % 2)
    b += str(sum(map(int, b)) % 2)
    if int(b, 2) > 45:
        print(i)  # 11
        break


# https://stepik.org/lesson/770696/step/12?unit=773131
for i in range(1, 100):
    b = bin(i)[2:]
    b += str(sum(map(int, b)) % 2)
    b += str(sum(map(int, b)) % 2)
    if int(b, 2) > 105:
        print(i)  # 26
        break


# https://stepik.org/lesson/770696/step/12?unit=773131
for i in range(1, 100):
    b = bin(i)[2:]
    b += str(sum(map(int, b)) % 2)
    b += str(sum(map(int, b)) % 2)
    if int(b, 2) > 99:
        print(int(b, 2))  # 102
        break


# https://stepik.org/lesson/770696/step/15?unit=773131
for i in range(1, 100):
    b = bin(i)[2:]
    b += b[-1]
    b += ['0', '1'][sum(map(int, b)) % 2]
    b += str(sum(map(int, b)) % 2)
    if int(b, 2) > 100:
        print(i)  # 13
        break


# https://stepik.org/lesson/770696/step/16?unit=773131
for i in range(2, 100):
    b = bin(i)[2:]
    b += b[-1]
    b += b[0]
    n = int(b, 2)
    if n > 170:
        print(i)  # 43
        break


""" 32.2 Обработка чисел в двоичном представлении. Часть 2 """
# https://stepik.org/lesson/1041386/step/2?unit=1049863
for i in range(1, 100):
    b = bin(i)[2:]
    if not sum(map(int, b)) % 2:
        b = '10' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'
    if int(b, 2) > 50:
        print(i)  # 19
        break


# https://stepik.org/lesson/1041386/step/3?unit=1049863
ls = []
for i in range(1, 100):
    b = bin(i)[2:]
    if not sum(map(int, b)) % 2:
        b += '0'
        b = '10' + b[2:]
    else:
        b += '1'
        b = '11' + b[2:]
    n = int(b, 2)
    if n > 45:
        ls.append((n, i))
ls.sort(key=lambda x: x[0])
print(ls[0])  # (46, 23)
print(ls[0][1])  # 23


# наименьшее значение R, большее 50 !!!
# https://stepik.org/lesson/1041386/step/4?unit=1049863
ls = []
for n in range(1, 1000):
    b = f'{n:b}'
    if not sum(map(int, b)) % 2:
        b = '1' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'
    if int(b, 2) > 50:
        ls.append((int(b, 2), n))
print(sorted(ls)[0])  # (51, 25)


# https://stepik.org/lesson/1041386/step/5?unit=1049863
ls = []
for n in range(1, 100):
    b = f'{n:b}'
    if not sum(map(int, b)) % 2:
        b = '1' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'
    if int(b, 2) > 25:
        ls.append((int(b, 2), n))
print(sorted(ls)[0][1])  # 29


# https://stepik.org/lesson/1041386/step/7?unit=1049863
ls = []
for n in range(1, 100):
    b = bin(n)[2:]
    if not n % 3:
        b += b[-3:]
    else:
        b += bin((n % 3) * 3)[2:]
    r = int(b, 2)
    if r > 100:
        ls.append((r, n))
ls.sort(key=lambda x: x[1])
print(ls[0])  # (118, 14)
print(ls[0][1])  # 14


# https://stepik.org/lesson/1041386/step/8?unit=1049863
ls = []
for n in range(1, 100):
    b = bin(n)[2:]
    if not n % 3:
        b += b[-3:]
    else:
        b += bin((n % 3) * 3)[2:]
    r = int(b, 2)
    if r < 50:
        ls.append((r, n))
ls.sort(key=lambda x: -x[1])
print(ls[0])  # (43, 10)
print(ls[0][1])  # 10


# https://stepik.org/lesson/1041386/step/9?unit=1049863
ls = []
for n in range(1, 100):
    b = bin(n)[2:]
    if not n % 3:
        b += b[-3:]
    else:
        b += bin((n % 3) * 3)[2:]
    r = int(b, 2)
    if r > 76:
        ls.append((r, n))
ls.sort(key=lambda x: x[1])
print(ls[0])  # (94, 11)
print(ls[0][1])  # 11


# https://stepik.org/lesson/1041386/step/10?unit=1049863
ls = []
for n in range(1, 100):
    b = bin(n)[2:]
    if not n % 3:
        b += b[-3:]
    else:
        b += bin((n % 3) * 3)[2:]
    r = int(b, 2)
    if r < 76:
        ls.append((r, n))
ls.sort(key=lambda x: -x[1])
print(ls[0])  # (67, 16)
print(ls[0][1])  # 16


# https://stepik.org/lesson/1041386/step/11?unit=1049863
ls = []
for n in range(1, 100):
    b = bin(n)[2:]
    if not n % 3:
        b += b[-3:]
    else:
        b += bin((n % 3) * 3)[2:]
    r = int(b, 2)
    if r <= 170:
        ls.append((r, n))
ls.sort(key=lambda x: -x[0])
print(ls[0])  # (166, 20)
print(ls[0][0])  # 166


""" 32.3 Обработка чисел в десятичном представлении """
# https://stepik.org/lesson/771159/step/3?unit=773604
for n in range(10, 100):
    b = f'{n % 2}{n % 3}{n % 5}'
    if b == '120':
        print(n)  # 35
        break


# https://stepik.org/lesson/771159/step/4?unit=773604
cnt = 0
for n in range(10, 100):
    r = f'{n % 4}{n % 3}{n % 2}'
    cnt += (r == '210')
print(cnt)  # 8


# https://stepik.org/lesson/771159/step/6?unit=773604
for n in range(100, 1000):
    s = str(n)
    a = sum(map(int, s[:2]))
    b = sum(map(int, s[1:]))
    r = sorted((a, b), reverse=True)
    if ''.join(map(str, r)) == '1712':
        print(n)  # 398
        break


# https://stepik.org/lesson/771159/step/7?unit=773604
for n in range(999, 99, -1):
    s = str(n)
    a = sum(map(int, s[:2]))
    b = sum(map(int, s[1:]))
    r = sorted((a, b), reverse=True)
    if ''.join(map(str, r)) == '1712':
        print(n)  # 984
        break


# https://stepik.org/lesson/771159/step/8?unit=773604
from math import prod
for n in range(100, 1000):
    s = str(n)
    a = prod(map(int, s[:2]))
    b = prod(map(int, s[1:]))
    r = sorted((a, b), reverse=True)
    if ''.join(map(str, r)) == '1612':
        print(n)  # 344
        break
