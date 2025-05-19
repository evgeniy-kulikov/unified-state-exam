"""
Task 23
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""

# https://stepik.org/lesson/552239/step/11?unit=545967
"""
1. Прибавь 1
2. Умножь на 2 и вычти 3
Сколько различных результатов можно получить из исходного числа  3 после выполнения программы, содержащей ровно 12 команд?
"""
res = set()
def fn(start, cnt):
    if cnt == 0:
        res.add(start)
        return 0
    fn(start + 1, cnt - 1)
    fn(start * 2 - 3, cnt - 1)
fn(3, 12)
print(len(res))  # 377
# print(res)


res = set()
res.add(3)
for cnt in range(12):
    can_get = set()
    for i in res:
        can_get.add(i + 1)
        can_get.add(i * 2 - 3)
    res = can_get
print(len(res))  # 377

# https://stepik.org/lesson/552239/step/12?unit=545967
"""
1. Прибавь 1
2. Умножь на 2
3. Сделай нечётное
Сколько существует таких программ, которые исходное число 3 преобразуют в число 25 
и при этом траектория вычислений программы содержит число 9 и число 17?
"""
def fn(st, end):
    if st > end:
        return 0
    if st == end:
        return 1
    return fn(st + 1, end) + fn(st * 2, end) + fn(st + st % 2 + 1, end)
print(fn(3, 9) * fn(9, 17) * fn(17, 25))  # 229635


# https://stepik.org/lesson/552239/step/13?unit=545967
"""
1. Вычти 8
2. Раздели нацело на 2
Сколько существует таких программ, которые исходное число 102 преобразуют в число 5 
и при этом траектория вычислений программы содержит число 43?
"""
def fn(st, end):
    if st < end:
        return 0
    if st == end:
        return 1
    return fn(st - 8, end) + fn(st // 2, end)
print(fn(102, 43) * fn(43, 5))  # 8


# https://stepik.org/lesson/552239/step/14?unit=545967
"""
двоичное число:
1. Прибавить 1
2. Добавить справа 0
3. Добавить справа 1
Сколько существует программ, которые исходное двоичное число 100 преобразуют в двоичное число 11101?
"""
def fn(st, end):
    if st > end:
        return 0
    if st == end:
        return 1
    return fn(st + 1, end) + fn(st * 2, end) + fn(st * 2 + 1, end)
print(fn(int('100', 2), int('11101', 2)))  # 79


# https://stepik.org/lesson/552239/step/14?unit=545967
"""
1. Прибавить 1
2. Прибавить 5
3. Умножить на 3
Определите число, для получения которого из числа 1 существует 175 программ.
"""
cnt = 0
def fn(st, end):
    if st > end:
        return 0
    if st == end:
        return 1
    return fn(st + 1, end) + fn(st + 5, end) + fn(st * 3, end)

for i in range(2, 1000):
    if fn(1, i) == 175:
        print(i)  # 19
        break

