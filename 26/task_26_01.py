"""
Task 26
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

# https://stepik.org/lesson/666350/step/7?unit=664353
from math import prod
from statistics import mean

with open('2.txt') as fl:
    f = list(map(int, fl))
print(sum(f), prod(f), mean(f))


# https://stepik.org/lesson/666350/step/10?unit=664353
with open('26.txt') as fl:
    size = int(next(fl).split()[0])  # 8200
    ls = sorted(map(int, fl))
cnt, sm = 0, 0
for i in range(len(ls)):
    if sm + ls[i] < size:
        cnt += 1
        sm += ls[i]
    else:
        sm -= ls[i - 1]  # убираем переполнение
        break
tail = size - sm  # 53  свободное место после сохранения первых (n-1) файлов
add = [i for i in ls[cnt - 1:] if i <= tail]
max_fl = max(add)
pass
print(cnt, max_fl)  # 568 50


# https://stepik.org/lesson/666350/step/11?unit=664353
with open('26_z1.txt') as fl:
    size = int(next(fl).split()[0])
    ls = sorted(map(int, fl))
cnt, sm = 0, 0
for i in range(len(ls)):
    if sm + ls[i] < size:
        cnt += 1
        sm += ls[i]
    else:
        sm -= ls[i - 1]
        break
tail = size - sm
add = [i for i in ls[cnt - 1:] if i <= tail]
max_fl = max(add)
print(cnt, max_fl)  # 206 33
# У автора ошибка


# https://stepik.org/lesson/666350/step/15?unit=664353
with open('26_z5.txt') as fl:
    size = int(next(fl).split()[0])
    ls = sorted(map(int, fl), reverse=True)
cnt, sm = 0, 0
for i in range(len(ls)):
    if sm + ls[i] <= size:
        cnt += 1
        sm += ls[i]
    else:
        break

if sm == size:
    print(cnt, ls[cnt])
else:
    tail = size - sm
    add = [i for i in ls if i <= tail]
    max_fl = max(add)
    print(cnt + 1, max_fl)  # 62 23


# https://stepik.org/lesson/666350/step/16?unit=664353
with open('26_z6.txt') as fl:
    size = int(next(fl).split()[0])
    ls = sorted(map(int, fl), reverse=True)
cnt, sm = 0, 0
for i in range(len(ls)):
    if sm + ls[i] <= size:
        cnt += 1
        sm += ls[i]
    else:
        break

if sm == size:
    print(cnt, ls[cnt])
else:
    tail = size - sm
    add = [i for i in ls if i <= tail]
    max_fl = max(add)
    print(cnt + 1, max_fl)  # 59 10


# https://stepik.org/lesson/666351/step/2?unit=664354
with open('26_2_z1.txt') as fl:
    size = int(next(fl).split()[1])
    ls = sorted(map(int, fl), reverse=True)
win = ls[:size]
laur = ls[size:size * 2]
print(laur[0], int(sum(win) / size)) # 131 14


# https://stepik.org/lesson/666351/step/8?unit=664354
with open('26_2022.txt') as fl:
    _ = next(fl)  # лишняя строка
    box = sorted(map(int, fl), reverse=True)
    res = [box[0]]  # кладем самую большую коробку
    for i in box:
        if abs(i - res[-1]) >= 3:  # сравниваем текушую коробку с последней коробкой финального списка
            res.append(i)
print(len(res), res[-1])


# https://stepik.org/lesson/666351/step/9?unit=664354
with open('26_2022.txt') as fl:
    _ = next(fl)  # лишняя строка
    box = sorted(map(int, fl), reverse=True)
    res = [box[0]]
    for i in box:
        if abs(i - res[-1]) >= 4:
            res.append(i)
print(len(res), res[-1])