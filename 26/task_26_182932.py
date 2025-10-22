""""""
"""
Task 26
Информатика Подготовка к ЕГЭ 2026
https://stepik.org/course/182932
"""


""" 25.1 Работа с сортировкой, отбором данных """

# https://stepik.org/lesson/1258750/step/2?unit=1272748
with open('add/course_182932/26_12933.txt') as fl:
# with open('add/test.txt') as fl:
    N, K = map(int, fl.readline().split())
    ls = [list(map(int, i.split())) for i in fl.readlines()]
    [ls[i].append(i + 1) for i in range(N)]

    ls_1 = [i for i in ls if i[0] < i[1]]  # шлифовка
    ls_2 = [i for i in ls if i[1] < i[0]]  # окрашивание
    ls_1.sort()
    ls_2.sort(key=lambda x: -x[1])
    ls = ls_1 + ls_2

    res_1 = len(ls_1)
    res_2 = ls[K-1][2]
    print(res_1, res_2)  # 489 920


# https://stepik.org/lesson/1258750/step/3?unit=1272748
with open('add/course_182932/26_12256.txt') as fl:
    S, N = map(int, fl.readline().split())
    ls = list(map(int, fl.readlines()))
    ls.sort()
    w = 0
    cnt = 0
    tail = 0
    for i in range(N):
        if w + ls[i] <= S:
            cnt += 1
            w += ls[i]
        else:
            w -= ls[i - 1]
            tail = S - w
            break
    add = max(i for i in ls if i <= tail)
    print(cnt, add)  # 629 50


# https://stepik.org/lesson/1258750/step/4?unit=1272748
with open('add/course_182932/26_8512.txt') as fl:
    K = int(fl.readline())  # ячейки
    N = int(fl.readline())  # пассажиры
    user = sorted([*map(int, i.split())] for i in fl.readlines())
    cell = [0] * K
    cnt = 0
    end = None
    for u in range(len(user)):
        for c in range(K):
            if cell[c] < user[u][0]:
                cell[c] = user[u][1]
                cnt += 1
                end = c + 1
                break
    print(cnt, end)  # 389 133


# https://stepik.org/lesson/1258750/step/5?unit=1272748
with open('add/course_182932/26_4712.txt') as fl:
    N = int(fl.readline())  # коробки
    box = sorted(map(int, fl), reverse=True)
    cur = box[0]
    cnt = 1
    for i in range(1, N):
        if cur - box[i] >= 3:
            cnt += 1
            cur = box[i]
    print(cnt, cur)  # 2767 51


# https://stepik.org/lesson/1258750/step/6?unit=1272748
with open('add/course_182932/26_4629.txt') as fl:
    N = int(fl.readline())  # 10_000
    # магазин делает скидку для 250-ти самых дешевых товаров,
    # а покупатель надеется получить скидку с 250-ти самых дорогих товаров
    goods = sorted(map(int, fl))  # сортируем мы, а не покупатель!!!
    idx = N // 4  # 250
    user_sale = sum(goods[N - idx:]) / 2  # ожидание скидки для покупателя
    store_sale = sum(goods[:idx]) / 2  # реальная скидка от магазина

    user = sum(goods[:- idx]) + user_sale
    store = sum(goods[idx:]) + store_sale
    print(int(user), int(store))  # 39434611 48825239

    # лучшая стратегия для покупателя будет просто отсортировать товары по цене (по убыванию)
    # strategy = sum(k for i, k in enumerate(goods) if not i % 4) / 2 + sum(k for i, k in enumerate(goods) if i % 4)
    # print(strategy)  # 44101521
    # print(int(sum(goods)))  # 50399596
