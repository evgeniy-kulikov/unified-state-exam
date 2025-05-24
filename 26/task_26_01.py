"""
Task 26
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

""" 26.1 Решение задач 1 """

# https://stepik.org/lesson/666350/step/5?unit=664353
with open('add/course_100138/1.txt') as fl:
    f = sorted(map(int, fl))
    print(*f)

# https://stepik.org/lesson/666350/step/6?unit=664353
from math import prod
from statistics import mean
with open('add/course_100138/2.txt') as fl:
    f = list(map(int, fl))
    print(sum(f), prod(f), mean(f))


# https://stepik.org/lesson/666350/step/7?unit=664353
with open('add/course_100138/3.txt') as fl:
    f = sorted(map(int, fl))
print(f[1], f[-2])


# https://stepik.org/lesson/666350/step/8?unit=664353
from math import prod
from statistics import mean
with open('add/course_100138/4.txt') as fl:
    f = list(map(int, fl))
avr = mean(f)
med = median(f)
print(int(abs(avr - med)))


# https://stepik.org/lesson/666350/step/9?unit=664353
with open('add/course_100138/5.txt') as fl:
    f = sorted(map(int, fl))
for i in range(2, len(f)):
    if sum(f[:i]) > f[-1]:
        print(i - 1)  # 3
        break


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




""" 26.2 Решение задач 2 """

# https://stepik.org/lesson/666351/step/2?unit=664354
with open('26_2_z1.txt') as fl:
    size = int(next(fl).split()[1])
    ls = sorted(map(int, fl), reverse=True)
win = ls[:size]
laur = ls[size:size * 2]
print(laur[0], int(sum(win) / size)) # 131 140


# https://stepik.org/lesson/666351/step/3?unit=664354
from statistics import mean
with open('add/course_100138/26_2_z2.txt') as fl:
    _, k, m = map(int, next(fl).split())
    f = sorted(map(int, fl))
    print(f[-k], int(mean(f[-(m+k):-k])))  # 144 137


# https://stepik.org/lesson/666351/step/4?unit=664354
from statistics import mean
with open('add/course_100138/26_2_z3.txt') as fl:
    n, k = map(int, next(fl).split())
    f = sorted(map(int, fl))
    print(int(mean(f[n - k:])), f[n - k - 1])  # 282 264


# https://stepik.org/lesson/666351/step/5?unit=664354
from statistics import mean
with open('add/course_100138/26_2_z4.txt') as fl:
    n, k, m = map(int, next(fl).split())
    f = sorted(map(int, fl))
    print(int(mean(f[n - k:])), f[n - k - 1], n - k - m)  # 282 264 140


# https://stepik.org/lesson/666351/step/6?unit=664354
from statistics import mean
with open('add/course_100138/26_2_z5.txt') as fl:
    n = int(next(fl))
    t = n // 10  # 20
    f = sorted(map(int, fl))
    print(f[-t - 1], f[t], int(mean(f[t:-t])))  # 680 515 594


# https://stepik.org/lesson/666351/step/7?unit=664354
from statistics import mean
with open('add/course_100138/26_2_z6.txt') as fl:
    n, k = map(int, next(fl).split())
    f = sorted(map(int, fl))
med = int(mean(f[k: -k]))  # 604
avr = f[n // 2]  # 603
i_1 = n // 2
i_2 = 0
for i in range(n):
    if f[i] > med:
        i_2 = i
        break
print(f[i_1  - 1: i_2 + 1])  # [602, 603, 605] # между 604 и 603 (включительно) находится 1 элемент
print(med, avr)  # 604 603 1


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



""" 26.3 Решение задач 3 """