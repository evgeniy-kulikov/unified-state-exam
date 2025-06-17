"""
Task 26
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""


""" 7.42 ЕГЭ Тренировка 26 """
# https://stepik.org/lesson/504397/step/1?auth=login&unit=496245
with open('add/course_57248/26-k3.txt') as fl:
    n, k, m = map(int, next(fl).split())
    d = sorted(map(int, fl), reverse=True)
    print(d[m + k - 1], d[k - 1])  # 519 909
# print(519, 909)


# https://stepik.org/lesson/504397/step/2?auth=login&unit=496245
from statistics import median, mean
cnt = 0
with open('add/course_57248/26-J2.txt') as fl:
    n = int(next(fl).strip())
    d = list(map(int, fl))
    avr = mean(d)
    med = median(d)
    a, m = min(avr, med), max(avr, med)
    for i in d:
        cnt += a <= i <= m
print(cnt)  # 340
# print(340)


# https://stepik.org/lesson/504397/step/3?auth=login&unit=496245
with open('add/course_57248/26-j4.txt') as fl:
    n = int(next(fl).strip())
    d = sorted(map(int, fl))
    tail = len(d) // 10  # 1000
mx = d[-tail-1]
size = sum(d[tail:-tail])
print(size, mx)
# print(440962, 91)


# https://stepik.org/lesson/504397/step/4?auth=login&unit=496245
""" жуткое для понимания условие задачи """
from math import ceil
with open('add/course_57248/26-s1.txt') as fl:
    n = int(next(fl).strip())
    d = sorted(map(int, fl))
for i in range(n):
    if d[i] > 100:
        idx = i  # индекс последнего товара который не участвует в скидке
        break
goods = d[i:]  # список пар: товар + товар со кидкой
sale_goods = goods[:len(goods) // 2]  # товары со кидкой
fool_goods = goods[len(goods) // 2:]  # товар с полной стоимостью
price_sale_goods = ceil(sum(sale_goods) * 0.9)  # общая стоимость товаров со скидкой
total = sum(d[:i]) + price_sale_goods + sum(fool_goods)
print(total, sale_goods[-1])
# print(499078, 550)


# https://stepik.org/lesson/504397/step/5?auth=login&unit=496245
f = open('add/course_57248/26-j7.txt')
n = int(f.readline())
d = sorted(map(int, f.readlines()), reverse=1)
total_tax = sum(d) * 0.6
reach_tax = sum(i * 0.8 for i in d[:n // 5])
poor_percent = (total_tax - reach_tax) / sum(d[n // 5:])
print(int(reach_tax), int(d[-1] * poor_percent))
# print(143518, 4)


# https://stepik.org/lesson/504397/step/6?auth=login&unit=496245
f = open('add/course_57248/26-k6.txt')
n, p = map(int, f.readline().split())  # кол-во пакетов, кол-во пакетов на отправку
d = [list(map(int, i.split())) for i in f.readlines()]  #  вес и стоимость
d.sort(key=lambda x: (x[1]/x[0], -x[0]))
weight = sum(i[0] for i in d[:p])
max_p = max((d), key=lambda x: x[0])
print(weight, max_p[1])
# print(5931, 800)


