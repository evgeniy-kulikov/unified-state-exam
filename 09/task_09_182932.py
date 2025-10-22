""""""
"""
Task 09
Информатика Подготовка к ЕГЭ 2026
https://stepik.org/course/182932
"""

# https://stepik.org/lesson/1210202/step/9?unit=1223456
cnt = 0
with open('9_4637.txt') as fl:
    for f in fl:
        a, b, c, d = sorted(map(int, f.split()))
        cnt += d**3 >= 2*a*b*c and all(i > 10 for i in [a, b, c, d])
print(cnt)  # 1820


# https://stepik.org/lesson/1210202/step/9?unit=1223456
cnt = 0
with open('add/course_182932/9_5126.txt') as fl:
    for f in fl:
        d = [*map(int, f.split())]
        n_1 = [i for i in d if d.count(i) == 1]
        n_3 = [i for i in d if d.count(i) == 3]
        if n_1 and n_3:
            cnt += len(n_1) == 3 and sum(n_1) / 3 <= sum(n_3)
print(cnt)  # 125


# https://stepik.org/lesson/1210202/step/10?unit=1223456
cnt = 0
with open('add/course_182932/9_5284.txt') as fl:
    for f in fl:
        d = sorted(map(int, f.split()))
        n_1 = [i for i in d if d.count(i) == 1]
        n_3 = [i for i in d if d.count(i) == 3]
        a = all([n_1, n_3, len(n_1) == 3])
        b = (d[0] + d[-1]) ** 2 > sum(i**2 for i in d[1:-1])
        cnt += a or b
print(cnt)  # 4209


# https://stepik.org/lesson/1210202/step/11?unit=1223456
cnt = 0
with open('add/course_182932/9_9740.txt') as fl:
    for f in fl:
        d = [*map(int, f.split())]
        n_1 = [i for i in d if d.count(i) == 1]
        n_3 = [i for i in d if d.count(i) == 3]
        if all([n_1, n_3, len(n_1) == 4]):
            cnt += sum(n_1) / 4 <= n_3[0]
print(cnt)  # 36


# https://stepik.org/lesson/1210202/step/12?unit=1223456
cnt = 0
with open('add/course_182932/09_9778.txt') as fl:
    for f in fl:
        cnt += 1
        d = [*map(int, f.split())]
        n_1 = [i for i in d if d.count(i) == 1]
        n_2 = [i for i in d if d.count(i) == 2]
        if all([n_1, n_2, len(n_1) == 4]):
            if n_2[0] >= sum(n_1) / 4:
                print(cnt)  # 34
                break


# https://stepik.org/lesson/1210202/step/13?unit=1223456
with open('add/course_182932/9_9832.txt') as fl:
    for f in fl:
        d = [*map(int, f.split())]
        n_1 = [i for i in d if d.count(i) == 1]
        n_2 = [i for i in d if d.count(i) == 2]
        if all([n_1, n_2, len(n_1) == 3]) and max(d) not in n_2:
            print(sum(d))  # 261
            break

# https://stepik.org/lesson/1210202/step/14?unit=1223456
cnt = 0
with open('add/course_182932/09_8609.txt') as fl:
    for f in fl:
        d = sorted(map(int, f.split()))
        cnt += len(set(d)) == 5 and (d[0] + d[-1]) * 2 <= sum(d[1:-1]) * 3
    print(cnt)  # 2776


# https://stepik.org/lesson/1210202/step/15?unit=1223456
from statistics import mean
cnt = 0
with open('add/course_182932/09_6357.txt') as fl:
    for f in fl:
        d = sorted(map(int, f.split()))
        n_1 = [i for i in d if d.count(i) == 1]
        n_2 = [i for i in d if d.count(i) > 1]
        if n_1 and n_2:
            cnt += mean(n_1) < mean(n_2)
    print(cnt)  # 1770


# https://stepik.org/lesson/1210202/step/16?unit=1223456
cnt = 0
with open('add/course_182932/09_10910.txt') as fl:
    for f in fl:
        d = sorted(map(int, f.split()))
        rep = [i for i in d if d.count(i) > 1]
        if rep and d[0] not in rep:
            cnt += d[0] + d[-1] < sum(rep)
    print(cnt)  # 447

