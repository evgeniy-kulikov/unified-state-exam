""""""
"""
Task 12
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""


""" 17.2 Практика (ур. базовый) """
# https://stepik.org/lesson/1223103/step/1?unit=1236592
for n in range(6, 100):
    s = "1" + '3' * n
    while any(['12' in s, '233' in s, '3333' in s]):
        s = s.replace('12', '332', 1)
        s = s.replace('233', '23', 1)
        s = s.replace('3333', '32', 1)
    if not sum(map(int, s)) % 6:
        print(n)  # 20
        break


# https://stepik.org/lesson/1223103/step/1?unit=1236592
for n in range(1000, 2, -1):
    s = "3" + '5' * n
    while any(['25' in s, '355' in s, '555' in s]):
        s = s.replace('25', '32', 1)
        s = s.replace('355', '25', 1)
        s = s.replace('555', '3', 1)
    if s.count('2') == 5:
        print(n)  #  21
        break


# https://stepik.org/lesson/1223103/step/3?unit=1236592
for n in range(1000):
    s = '3' + '0' * 40 + '1' * n + '2' * 40
    while any(['31' in s, '32' in s, '30' in s]):
        s = s.replace('31', '223', 1)
        s = s.replace('32', '23', 1)
        s = s.replace('30', '13', 1)
    s = s.replace('3', '0', 1)
    r = str(sum(map(int, s)))
    if len(r) == 3 and len(set(r)) == 1:
        print(n)  # 81
        break

# https://stepik.org/lesson/1223103/step/4?unit=1236592
s = '3' + '4' * 60 + '6' * 60 + '8' * 60
while any(['46' in s, '84' in s, '86' in s]):
    s = s.replace('46', '64', 1)
    s = s.replace('84', '48', 1)
    s = s.replace('86', '68', 1)
res = [s[24], s[74], s[149]]
print(''.join(res))  # 648


# https://stepik.org/lesson/1223103/step/5?unit=1236592
s = '1' * 38 + '2' * 34 + '3' * 30
while any(['33' in s, '11' in s, '22' in s]):
    s = s.replace('33', '12', 1)
    s = s.replace('11', '32', 1)
    s = s.replace('22', '31', 1)
print(sum(map(int, s)))  # 208


# https://stepik.org/lesson/1223103/step/6?unit=1236592
from math import prod
s = '7' * 333
while any(['66' in s, '77777' in s]):
    if '66' in s:
        s = s.replace('66', '7', 1)
    else:
        s = s.replace('77777', '676676', 1)
print(prod(map(int, s)))  # 366087922704


# https://stepik.org/lesson/1223103/step/7?unit=1236592
s = '1' + '0' * 105
while '1' in s:
    if '100' in s:
        s = s.replace('100', '0001', 1)
    else:
        s = s.replace('1', '00', 1)
print(s.count('0'))  # 159


# https://stepik.org/lesson/1223103/step/8?unit=1236592
s = '>' + '432' * 100 + '<'
while any(['>4' in s, '>3' in s, '>2' in s, '<4' in s, '<3' in s, '<2' in s]):
    if '>4' in s or '>3' in s:
        s = s.replace('>4', '2>3', 1)
        s = s.replace('>3', '1>2', 1)
    elif '<4' in s or '<3' in s:
        s = s.replace('4<', '3<2', 1)
        s = s.replace('3<', '2<1', 1)
    else:
        s = s.replace('>2', '0>', 1)
        s = s.replace('<2', '0<', 1)
s = s.replace('<', '').replace('>', '')
print(sum(map(int, s)))  # 400


# https://stepik.org/lesson/1223103/step/9?unit=1236592
s = '2' + '5' * 81
while any(['25' in s, '355' in s, '4555' in s]):
    s = s.replace('25', '4', 1)
    s = s.replace('355', '2', 1)
    s = s.replace('4555', '3', 1)
print(s)  # 455


# https://stepik.org/lesson/1223103/step/10?unit=1236592
for n in range(4, 1000):
    s = '2' + '5' * n
    while any(['25' in s, '355' in s, '555' in s]):
        s = s.replace('25', '5', 1)
        s = s.replace('355', '52', 1)
        s = s.replace('555', '3', 1)
    if s.count('3') == 2:
        print(n)  #  18
        break


# https://stepik.org/lesson/1223103/step/11?unit=1236592
for n in range(4, 10_000):
    s = '5' + '2' * n
    while any(['52' in s, '2222' in s, '1122' in s]):
        s = s.replace('52', '11', 1)
        s = s.replace('2222', '5', 1)
        s = s.replace('1122', '25', 1)
    if sum(map(int, s)) % 10 == 7:
        print(n)  #  5
        break


# https://stepik.org/lesson/1223103/step/12?unit=1236592
mx = 0
for n in range(4, 10_000):
    s = '3' + '5' * n
    while any(['333' in s, '555' in s]):
        if '555' in s:
            s = s.replace('555', '3', 1)
        else:
            s = s.replace('333', '5', 1)
    mx = max(mx, sum(map(int, s)))
print(mx)  # 26


# https://stepik.org/lesson/1223103/step/13?unit=1236592
for n in range(1000, 3, -1):  # 10_000 излишне
    s = '5' + '2' * n
    while any(['52' in s, '2222' in s, '1122' in s]):
        s = s.replace('52', '11', 1)
        s = s.replace('2222', '5', 1)
        s = s.replace('1122', '25', 1)
    if sum(map(int, s)) == 64:
        print(n)  # 156
        break

# https://stepik.org/lesson/1223103/step/14?unit=1236592
mx = 0
for n in range(4, 1_000):  # 10_000 излишне
    s = '5' + '7' * n
    while any(['57' in s, '877' in s, '777' in s]):
        s = s.replace('57', '7', 1)
        s = s.replace('877', '75', 1)
        s = s.replace('777', '8', 1)
    mx = max(mx, sum(map(int, s)))
print(mx)  # 59


# https://stepik.org/lesson/1223103/step/15?unit=1236592
mx = 0
for n in range(210, 300):
    s = '3' + '7' * n
    while any(['27' in s, '377' in s, '777' in s]):
        s = s.replace('27', '32', 1)
        s = s.replace('377', '27', 1)
        s = s.replace('777', '3', 1)
    if not sum(map(int, s)) % 15:
        mx = max(mx, n)
print(mx)  # 287


# https://stepik.org/lesson/1223103/step/16?unit=1236592
mx = 0
for n in range(4, 1000):
    s = '1' + '2' * n
    while any(['12' in s, '322' in s, '222' in s]):
        s = s.replace('12', '2', 1)
        s = s.replace('322', '21', 1)
        s = s.replace('222', '3', 1)
    mx = max(mx, len(s))
print(mx)  # 9




""" 17.3 Практика (ур. усложненный) """
# https://stepik.org/lesson/1223104/step/1?unit=1236593
def f(n):
    return all(n % i for i in range(2, int(n**0.5 + 1)))

for n in range(100):
    s = '>' + '0' * 37 + '1' * n + '2' * 37
    while any(['>1' in s, '>2' in s, '>0' in s]):
        s = s.replace('>1', '22>', 1)
        s = s.replace('>2', '2>', 1)
        s = s.replace('>0', '1>', 1)
    r = sum(map(int, s.replace('>', '')))
    if f(r):
        print(n)  # 4
        break


# https://stepik.org/lesson/1223104/step/2?unit=1236593
cnt = 0
s = '7' * 512
while '7777' in s or '1111' in s:
    if '7777' in s:
        s = s.replace('7777', '1', 1)
        cnt += 1
    else:
        s = s.replace('1111', '7', 1)
        cnt += 1
print(cnt)  # 170


# https://stepik.org/lesson/1223104/step/3?unit=1236593
for n in range(1, 1000):
    cnt = 0
    s = '3' * n
    while '3333' in s or '222' in s:
        if '3333' in s:
            s = s.replace('3333', '2', 1)
            cnt += 1
        else:
            s = s.replace('222', '3', 1)
            cnt += 1
    if s == '22' and cnt == 34:
        print(n)  # 96
        break


# https://stepik.org/lesson/1223104/step/4?unit=1236593
for n in range(1, 1000):
    s = '>' + '0'* 40 + '1' * n + '2' * 40
    while any(['>1' in s, '>2' in s, '>0' in s]):
        s = s.replace('>1', '22>', 1)
        s = s.replace('>2', '2>', 1)
        s = s.replace('>0', '1>', 1)
        r = str(sum(map(int, s.replace('>', ''))))
    if len(r) == 3 and len(set(r)) == 1:
        print(n)  # 81
        break


# https://stepik.org/lesson/1223104/step/5?unit=1236593
cnt = 0
s = '7' * 256
while any(['7777' in s, '1111' in s]):
    if '7777' in s:
        s = s.replace('7777', '1', 1)
        cnt += 4
    else:
        s = s.replace('1111', '7', 1)
print(cnt)  # 272


# https://stepik.org/lesson/1223104/step/6?unit=1236593
cnt = 0
for n in range(1, 101):
    s = '1' + '0' * n
    while any(['01' in s, '1' in s]):
        if '10' in s:
            s = s.replace('10', '0001', 1)
        elif '1' in s:
           s = s.replace('1', '0', 1)
    cnt += not len(s) % 7
print(cnt)  # 15



""" 17.4 Закрепление """
# https://stepik.org/lesson/1223105/step/12?unit=1236594
for n in range(1, 101):
    s = '1' * 200 + '1' * n
    while any(['111' in s, '222' in s]):
        s = s.replace('111', '22', 1)
        s = s.replace('222', '1', 1)
    if not s.count('1'):
        print(200 + n)  # 206
        break

