""""""
"""
https://kompege.ru/task
26. Обработка данных с помощью сортировки
"""


# № 23765 Демоверсия 2026 (Уровень: Базовый)
# https://vkvideo.ru/video-205865487_456240491?t=2h20m58s&ref_domain=kompege.ru
with open('add/kompege/26_23765.txt') as fl:
    n = int(fl.readline().strip())
    cnt = 1
    d = []
    for i in fl:
        tm = [*map(int, i.split())]
        ex = ('X', 'G')[tm.index(min(tm))]
        d.append(tuple(tm) + (ex, ) + (cnt,))
        cnt += 1
    d.sort(key=lambda x: min(x[:2]))
    print(d[-1])  # (97582, 97257, 'G', 564)
    print(d[-1][-1])  # 564
    print(sum(i[2] == 'G' for i in d) - 1)  # 444  >>> столько 'G' будет после (97582, 97257, 'G', 564)



# № 23383 Резервный день 19.06.25 (Уровень: Базовый)
# https://vkvideo.ru/video-205865487_456240489?t=1h15m52s&ref_domain=kompege.ru
# Длинный путь
with open('add/kompege/26_23383.txt') as fl:
    num = int(fl.readline().strip())
    data = dict()
    res = list()
    for f in fl:
        sport, point = map(int, f.split())
        data.setdefault(point, [])
        data[point] += [sport]

    for key in data:
        ls = sorted(set(data[key]))  # set() убрать повторяющиеся номера !!!
        cnt = 0
        c = 1
        for i in range(1, len(ls)):
            if ls[i] - ls[i - 1] == 1:  # благодаря ранее исп. set() теперь верно находится непрерывная цепочка
                c += 1
                cnt = max(cnt, c)
            else:
                c = 1
        res.append((cnt, key))

res.sort(key=lambda x: (-x[0], x[1]))
print(*res[0])  # 56 30113

# Короче
with open('add/kompege/26_23383.txt') as fl:
    next(fl)
    num = [tuple(map(int, i.split())) for i in fl]   # [0] номер спортсмена, [1] номер посещённой им точки
    num = sorted(set(num), key=lambda x: (x[1], x[0])) + [(-1, -1)]
    c = 1
    res = []
    for i in range(len(num) - 1):
        if num[i][1] == num[i + 1][1] and ((num[i + 1][0] - num[i][0]) == 1):
            c += 1
        else:
            res += [(num[i][1], c)]
            c = 1
    res.sort(key=lambda x: (-x[1], x[0]))
    print(*res[0])  # 30113 56



# № 23283 Основная волна 11.06.25 (Уровень: Базовый)
# https://vkvideo.ru/video-205865487_456240488?t=1h26m3s&ref_domain=kompege.ru
with open('add/kompege/26_23283.txt') as fl:
    windows, user = int(fl.readline()), int(fl.readline())
    time = [tuple(map(int, i.split())) for i in fl]  # [0] start   [1] end
    time.sort()
    win = [0] * (windows)
    cnt = 0
    last = 0
    for st, en in time:
        for i in range(windows):
            if win[i] < st:
                win[i] = en
                cnt += 1
                last = i
                break
print(cnt, last + 1)  # 793 2



# № 23208 Основная волна 10.06.25 (Уровень: Базовый)
# https://vkvideo.ru/video-205865487_456240487?t=1h29m31s&ref_domain=kompege.ru
conv = []
with open('add/kompege/26_23208.txt') as fl:
    _ = int(fl.readline())
    c = 1
    for f in fl:
        conv += [[*map(int, f.split())] + [c]]  # Шлифовка, Окрашивание, Номер
        c += 1
    for i in conv:
        d = min(i[:2])
        oper = (1, 0)[i.index(d)]
        i.extend([d, oper])  # 1 шлифовка, 0 окрашивание
        # [t1, t2, Номер, min([t1, t2]), 1/0]
    conv.sort(key=lambda x: x[3])
    print(conv[-1][2])  # 503
    print(sum(i[4] for i in conv) - conv[-1][-1])  # 478
# - conv[-1][-1]  если последняя деталь для шлифовки


