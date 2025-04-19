"""
Task 18
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""

# https://stepik.org/lesson/552239/step/6?unit=545967
# 18/add/course-57248/18-109.xls
# НЕ РЕШЕНО (

# https://stepik.org/lesson/552239/step/8?unit=545967
# 18/add/course-57248/18-116.xls
# НЕ РЕШЕНО (вероятна ошибка теста автора)

# https://stepik.org/lesson/552239/step/7?unit=545967
# 18/add/course-57248/18-114.xls

# https://stepik.org/lesson/552239/step/9?unit=545967
# 18/add/course-57248/18-118.xls

# https://stepik.org/lesson/499908/step/1?unit=491458
# 18/add/course-57248/18-11.xls

# https://stepik.org/lesson/499908/step/2?unit=491458
# 18/add/course-57248/18-0.xls

# https://stepik.org/lesson/499908/step/3?unit=491458
# 18/add/course-57248/18-2.xls

# https://stepik.org/lesson/499908/step/12?unit=491458
# 18/add/course-57248/18-1.xls


"""
решение без использования таблицы
"""
# https://stepik.org/lesson/499908/step/9?unit=491458
# решение без использования таблицы
with open('18-77.txt') as fl:
    ls = list(map(float, fl))
sm = -10_000_000
i_start = 0
for i in range(1, len(ls)):
    if abs(ls[i - 1] - ls[i]) <= 2:  # оцениваем хвост
        sm = max(sm, sum(ls[i_start: i + 1])) # постоянное накапливание и сравнение суммы
    else:
        i_start = i  # сдвигаем
print(int(sm))  # 58


# https://stepik.org/lesson/499908/step/11?unit=491458
with open('18-77-1.txt') as fl:
    ls = list(map(float, fl))
sm = -10_000_000
cursor = 0
for i in range(1, len(ls)):
    if abs(ls[i - 1] - ls[i]) >= 8 :
        sm = max(sm, sum(ls[cursor: i + 1]))
    else:
        cursor = i
print(int(sm))  # 46


# https://stepik.org/lesson/499908/step/11?unit=491458
with open('18-k3.txt') as fl:
    ls = list(map(int, fl))
res = 100_000
for i in range(len(ls) - 5):
    for k in range(i + 1, i + 6):
        sm = sum([ls[i], ls[k]])
        if not sm % 2:
            res = min(res, sm)
print(res) # 30

