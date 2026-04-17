

# https://stepik.org/lesson/687436/step/9?unit=686601
f = open('26_001.txt')
next(f)  # число не используется
data = [[*map(int, i.split())] for i in f]  # ряд / место
d = {i: set() for i in range(1, 10_001)}  # словарь с координатами точек матрицы
for i in data:
    k, v = i
    d[k].add(v)
res = [(sum(i % 2 for i in v), k) for k,v in d.items()]  #  кол-во светлых точек в нечётных местах ряда
res.sort(key=lambda x: (-x[0], x[1]))
print(*res[0])  # 17 8437



# https://stepik.org/lesson/703201/step/8?auth=login&unit=703534
f = open('26_002.txt')
_ = next(f)
data = [[*map(int, i.split())] for i in f]
d = dict()
for i in data:
    k, v = i
    d.setdefault(k, set())  # ряд / светлые места в ряду
    d[k].add(v)

row_group = []  # определение рядов с максимальными группами
for k, v in d.items():
    if v:
        mx = c = 1
        v = sorted(v)
        for i in range(len(v) - 1):
            if v[i+1] - v[i] == 1:
                c += 1
                mx = max(mx, c)
            else:
                c = 1
        row_group.append((k, mx, v))
row_group.sort(key=lambda x: -x[1])
mx_group = row_group[0][1]  # принимаем что в ряду только ОДНА группа имеет максимальную длину (иначе код переделать)
row_group = [i for i in row_group if i[1] == mx_group]

row_seat = []  # итоговое формирование рядов с подходящими местами
for el in row_group:
    c = 1
    v = el[2]
    for i in range(len(v) - 1):
        if v[i + 1] - v[i] == 1:
            c += 1
        else:
            c = 1
        if c == 6:
            row_seat.append((el[0], (v[i-4], v[i+1])))
            break

result = []
for i in row_seat:
    r, s = i[0], i[1]
    a = min(s[0] - 1, 10_000 - s[-1])
    b = min(r - 1, 10_000 - r)
    result.append((r, min([a, b])))
result.sort(key=lambda x: -x[1])
print(*result[0])  # 4697, 4574


