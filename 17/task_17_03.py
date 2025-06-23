""""""
"""
Task 16
ЕГЭ по информатике: варианты
https://stepik.org/course/228948
"""


# https://stepik.org/lesson/1599364/step/4?unit=1621008
with open('17_alles.txt') as fl:
    cnt = sm = 0
    d = list(map(int, fl))
    min_41 = min(i for i in d if i >= 41 and not i % 41)  # 984
    for i in range(len(d) - 1):
        a, b = d[i: i+2]
        if all([a != b, not abs(a - b) % min_41]):
            cnt += 1
            sm = max(sm, a + b)
print(cnt, sm)  # 10 92404


# https://stepik.org/lesson/1609596/step/4?unit=1631352
with open('17_alles.txt') as fl:
    cnt = mx3 = 0
    d = list(map(int, fl))
    mx = max(i for i in d if abs(i) % 100 == 25)  # 84725
    for k in range(len(d) - 2):
        n = d[k: k + 3]
        if len([i for i in n if len(str(abs(i))) == 4]) <= 2:
            if sum(n) <= mx:
                cnt += 1
                mx3 = max(mx3, sum(n))
    print(cnt, mx3)  # 6315 84523



