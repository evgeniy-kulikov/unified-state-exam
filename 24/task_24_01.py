"""
Task 24
ЕГЭ Питоныч
https://stepik.org/course/100138
Задание 24 КЕГЭ. Часть 1
Задание 24 КЕГЭ. Часть 2  --> task24_02
"""


""" 21.2 Поиск C-подцепочек """

# https://stepik.org/lesson/570933/step/4?unit=565502
st = input()
max_len = 0
cur_len = 0
for s in st:
    if s in 'BC':
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 0
print(max_len)  # 6


""" 21.3 Поиск произвольных подцепочек """

# https://stepik.org/lesson/570934/step/3?unit=565503
st = input()
max_len = 1
cur_len = 1
for i in range(1, len(st)):
    if st[i - 1] == st[i] :
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 1
print(max_len)  # 5


# https://stepik.org/lesson/570934/step/5?unit=565503
st = input()
max_len = 1
cur_len = 1
for i in range(1, len(st)):
    if st[i - 1] < st[i] :
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 1
print(max_len)  # 6


# https://stepik.org/lesson/570934/step/10?unit=565503
st = input()
max_len = 1
cur_len = 1
for i in range(1, len(st)):
    if st[i - 1:i + 1] != 'AB':
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 1
print(max_len)  # 22


# https://stepik.org/lesson/570934/step/12?unit=565503
st = input()
max_len = 1
cur_len = 2
for i in range(2, len(st)):
    if st[i - 2:i + 1] != 'EFF':
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 2
print(max_len)  # 26


# https://stepik.org/lesson/570934/step/14?unit=565503
st = input()
max_len = 1
cur_len = 3
for i in range(3, len(st)):
    if st[i - 3:i + 1] != 'ABCD':
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 3
print(max_len)  # 53



""" 21.4 Определение количества подцепочек """
# https://stepik.org/lesson/570935/step/3?unit=565504
st = input()
cnt = 0
for i in range(len(st) - 2):
    cnt += len(set(st[i:i+3])) == 1
print(cnt)  # 12


# https://stepik.org/lesson/570935/step/4?unit=565504
st = input()
cnt = 0
for i in range(len(st) - 2):
    s = st[i:i + 3]
    cnt += all((s[0] != s[1], s[1] != s[2]))
print(cnt)  # 28


# https://stepik.org/lesson/570935/step/5?unit=565504
st = input()
cnt = 0
for i in range(len(st) - 2):
    s = st[i:i + 3]
    cnt += all((s[0] in 'ACD', s[1] in 'BCF', s[1] == s[2]))
print(cnt)  # 4


# https://stepik.org/lesson/570935/step/6?unit=565504
st = input()
cnt = 0
for i in range(1, len(st) - 1):
    cnt += st[i - 1] < st[i] > st[i + 1]
print(cnt)  # 5


# https://stepik.org/lesson/570935/step/12?unit=565504
from re import findall
st = input()
reg = r'(?:D[EF])+'
mx = 0
for el in findall(reg, st):
    mx = max(mx, len(el) // 2)
print(mx)  # 8

# сишком длинно
st = input()
cnt_max = 0
cnt = 0
for i in range(0, len(st) - 1, 2):
    if st[i] == 'D' and st[i + 1] in 'EF':
        cnt += 1
    else:
        cnt_max = max(cnt_max, cnt)
        cnt = 0

cnt = 0 #  а нужно ли???
for i in range(1, len(st) - 1, 2):
    if st[i] == 'D' and st[i + 1] in 'EF':
        cnt += 1
    else:
        cnt_max = max(cnt_max, cnt)
        cnt = 0
print(cnt_max) # 8


# https://stepik.org/lesson/570935/step/13?unit=565504
from re import findall
# st = input()
reg = r'(?:1[02])+'
mx = 0
for el in findall(reg, st):
    mx = max(mx, len(el) // 2)
print(mx)  # 10


# https://stepik.org/lesson/570936/step/2?unit=565505
from re import findall
st = input()
reg = r'D+'
mx = 0
res = findall(reg, st)
for el in res:
    mx = max(mx, len(el))
print(mx, len(res), len(st))  # 5 4 67



""" 21.5 Решение задач """

# https://stepik.org/lesson/570936/step/5?unit=565505
st = input()
ch_max = st[0]
ln, ln_max = 1, 1
for i in range(1, len(st)):
    if st[i] == st[i - 1]:
        ln += 1
        if ln > ln_max:
            ln_max, ch_max = ln, st[i]
    else:
        ln = 1
print(ch_max, ln_max)


# https://stepik.org/lesson/570936/step/6?unit=565505
st = input()
ch_max = st[-1]
ln, ln_max = 1, 1
for i in range(1, len(st)):
    if st[i] == st[i - 1]:
        ln += 1
        if ln >= ln_max:
            ln_max, ch_max = ln, st[i]
    else:
        ln = 1
print(ch_max, ln_max)

# https://stepik.org/lesson/570936/step/7?unit=565505
st = input()
ch_max = st[0]
ln, ln_max = 1, 1
for i in range(1, len(st)):
    if st[i] != st[i - 1]:
        ln += 1
        if ln > ln_max:
            ln_max, ch_max = ln, st[i - ln_max:i + 1]
    else:
        ln = 1
print(ch_max, ln_max)


# https://stepik.org/lesson/570936/step/8?unit=565505
# !!! шаблон !!!
# Создаем словарь:
# ключ - индекс строки, с которо начинается нужное событие
# значение - отрезок строки, где происходит это событие
# Если флаг истина - можно создать ключ-значение
# Далее сортировка словаря в список (ключ сортировки - требованиям задания)
st = input()
d = dict()
key = 0
flag = True
for i in range(len(st) - 1):
    if st[i] < st[i + 1]:
        if flag:
            d.setdefault(i, st[i])
            key = i
            flag = False
        d[key] += st[i + 1]
    else:
        flag = True
res = [i for i in d.items()]
res.sort(key=lambda x: (-len(x[1]), x[0]))
if res:
    print(res[0][1] , len(res[0][1]))
else:
    print(st[0] , 1)  # хотелка автора

# короче, но легко запутаться
st = input()
ch_max = st[0]
ln, ln_max = 1, 1
for i in range(1, len(st)):
    if st[i] > st[i - 1]:
        ln += 1
        if ln > ln_max:
            ln_max, ch_max = ln, st[i - ln_max:i + 1]
    else:
        ln = 1
print(ch_max, ln_max)


# https://stepik.org/lesson/570936/step/9?unit=565505
st = input()
len_cur, len_max = 1, 1
i_cur, i_max = 0, 0
for i in range(len(st) - 1):
    if st[i] < st[i + 1]:
        len_cur += 1
        if len_cur == 2:
            i_cur = i
        if len_cur > len_max:
            len_max = len_cur
            i_max = i_cur
    else:
        len_cur = 1
print(i_max + 1)


# https://stepik.org/lesson/570936/step/10?unit=565505
# шаблон
st = input()
d = dict()
key = 0
flag = True
for i in range(len(st) - 1):
    if st[i] < st[i + 1]:
        if flag:
            d.setdefault(i, st[i])
            key = i
            flag = False
        d[key] += st[i + 1]
    else:
        flag = True
res = [i for i in d.items()]
res.sort(key=lambda x: (-len(x[1]), x[0]))
print(res[0][0] + 1 if res else 1)

# легко запутаться
st = input()
s_cur, s_max = st[0], ''
len_cur, len_max = 1, 1
i_cur, i_max = 0, 0
for i in range(len(st) - 1):
    if st[i] <= st[i + 1]:
        len_cur += 1
        if len_cur == 2:
            i_cur = i
        if len_cur > len_max:
            len_max = len_cur
            i_max = i_cur
            s_max = st[i_cur: i + 2]
    else:
        len_cur = 1
        s_cur = ''
print(s_max, len(s_max), i_max + 1)


# https://stepik.org/lesson/570936/step/11?unit=565505
st = input()
flag = True
ls = []
for i in range(1, len(st)):
    if st[i - 1] == st[i]:
        if flag:
            ls.append(st[i - 1])
            flag = False
        ls[-1] += st[i]
    else:
        flag = True

mx = max(map(len,ls))
res = [el for el in ls if len(el) == mx]
for el in res:
    print(el[0], len(el))


# https://stepik.org/lesson/570936/step/12?unit=565505
from re import findall
st = input()
reg = r'(?:ABC)+'
res = findall(reg, st)
print(max(map(len, res)) // 3 if res else 0)


# https://stepik.org/lesson/570936/step/14?unit=565505
from re import findall
st = input()
reg = r'\d+'
res = findall(reg, st)
if res:
    mx = max(map(len, res))
    ls = [el for el in res if len(el) == mx]
    print(mx, ls[0])


# https://stepik.org/lesson/570936/step/15?unit=565505
from re import findall
st = input()
reg = r'\d*[02468]'
res = findall(reg, st)
if res:
    print(max(map(int, res)))


# https://stepik.org/lesson/570936/step/16?unit=565505
# локальный минимум - это элемент, который меньше любого из своих соседей
# локальный максимум - это элемент, который больше любого из своих соседей
st = input()
mn, mx = 0, 0
for i in range(1, len(st) - 1):
    mx += st[i - 1] < st[i] > st[i + 1]
    mn += st[i - 1] > st[i] < st[i + 1]
print(mx, mn)








