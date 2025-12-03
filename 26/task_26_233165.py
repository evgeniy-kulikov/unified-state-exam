""""""
"""
Task 26
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 26.1 Задание 26 ЕГЭ | Урок 1 """
# https://stepik.org/lesson/1726034/step/2?unit=1749716
# https://kompege.ru/task   № 936 Джобс 08.02.2021 (Уровень: Сложный)
# made it myself
with open('add/course_233165/26-1_02.txt') as file:
    N, S = map(int, next(file).split())
    m = sorted(map(int, file), reverse=True)
    res = []
    while len(m):
        ship = []
        for i in range(len(m)):
            if sum(ship) + m[i] <= S:
                ship.append(m[i])
                m[i] = 0
        res.append(ship)
        m = [i for i in m if i]
    print(len(res), sum(res[-1]))  # 423 501


# https://stepik.org/lesson/1726034/step/3?unit=1749716
# https://kompege.ru/task   № 225 Джобс 14.09.2020 (Уровень: Базовый)
# made it myself
with open('add/course_233165/26-1_03.txt') as file:
    S, N = map(int, next(file).split())
    m = sorted(map(int, file), reverse=True)
    res = []
    for i in range(len(m)):
        if sum(res) + m[i] <= S:
            res.append(m[i])
            m[i] = 0
    m = [i for i in m if i]
    for i in range(len(m)):
        if sum(res) + m[i] <= S:
            res.append(m[i])
    print(len(res), res[-1])  # 1054 732


# https://stepik.org/lesson/1726034/step/4?unit=1749716
# https://kompege.ru/task   № 788 Джобс 30.11.2020 (Уровень: Средний)
with open('add/course_233165/26-1_04.txt') as file:
    D, E, N = map(int, next(file).split())  # 5000 1500
    m = sorted(map(int, file))

    ls_d = [i for i in m if i > 500]
    ls_d_end = []
    while sum(ls_d) > D:
        ls_d_end.append(ls_d.pop())
    ls_d_end.sort()
    d = D - sum(ls_d[:-1])
    for i in range(len(ls_d_end)):
        if ls_d_end[i] <= d:
            ls_d[-1] = ls_d_end[i]

    ls_e = [i for i in m if i <= 500]
    ls_e_end = []
    while sum(ls_e) > E:
        ls_e_end.append(ls_e.pop())
    ls_e_end.sort()
    e = E - sum(ls_e[:-1])
    for i in range(len(ls_e_end)):
        if ls_e_end[i] <= e:
            ls_e[-1] = ls_e_end[i]
print(len(ls_d) + len(ls_e), max(ls_d) + max(ls_e))  # 13 1381


# https://stepik.org/lesson/1726034/step/5?unit=1749716
# https://kompege.ru/task   № 2149 (Уровень: Базовый)
with open('add/course_233165/26-1_05.txt') as file:
    _, M = map(int, next(file).split())
    d = sorted(map(int, file))
    pic = [i for i in d if i <= 100]
    vid = [i for i in d if i > 100]
    usb = []
    for i in vid:
        if sum(usb) < M / 2:
            usb.append(i)
    for i in pic:
        if sum(usb) + i <= M:
            usb.append(i)
    if M - sum(usb):
        usb.pop()
    for i in pic[::-1]:
        if sum(usb) + i <= M:
            usb.append(i)
            break
    print(M - sum(usb), len(usb))  # 0 7347


# https://stepik.org/lesson/1726034/step/6?unit=1749716
# https://kompege.ru/task   № 1395 (Уровень: Базовый)
with open('add/course_233165/26-1_06.txt') as file:
    S, N = map(int, next(file).split())
    d = sorted(map(int, file))
    p = m = 0
    for i in range(N):
        if m + d[i] <= S:
            m += d[i]
            p = i
        else:
            break
    print(len(d[p+1:]), sum(d[p+1:]))  # 7655 542450




""" 26.4 Задание 26 ЕГЭ | Задачи прошлых лет """
# https://stepik.org/lesson/1726037/step/1?unit=1749719
# https://kompege.ru/task   № 9756 Основная волна 19.06.23 (Уровень: Средний)
data = open('add/course_233165/26-3_01.txt').readlines()
N = int(data[0])
ls = [tuple(map(int, i.split())) for i in data[1:]]
ls.sort(key=lambda x: (x[1], x[0]))
res = []
end = 0
for i in ls:
    st, en = i
    if st >= end:
        res.append(i)
        end = en
res.pop()
end = res[-1][1]
for i in ls[::-1]:
    if i[0] >= end:
        res.append(i)
        break
print(len(res), res[-1][1])  # 16 1345

