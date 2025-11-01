""""""
"""
Task 09
Подборка задач для подготовки к ЕГЭ по информатике 2026 | itpy
https://stepik.org/course/122969
"""


""" 4.7 Проверочная: Работа с файлами, номера: 9, 17, 24 """
# https://stepik.org/lesson/1231755/step/2?unit=1245338
cnt = 0
with open('add/course_122969/09_4_7_01.txt') as file:
    for fl in file:
        d = sorted(map(int, fl.split()))
        rep = [i for i in d if d.count(i) == 2]
        if rep:
            cnt += d[-1] < sum(d[:-1])
    print(cnt)  # 147

# https://stepik.org/lesson/1231755/step/3?unit=1245338
cnt = 0
with open('add/course_122969/09_4_7_02.txt') as file:
    for fl in file:
        d = sorted(map(int, fl.split()))
        if len(set(d)) == 5:
            cnt += (sum(d[1:-1]) * 3) / (d[0] + d[-1]) > 4
    print(cnt)  # 11420


# https://stepik.org/lesson/1231755/step/4?unit=1245338
cnt = 0
with open('add/course_122969/09_4_7_03.txt') as file:
    for fl in file:
        d = sorted(map(int, fl.split()))
        if len(set(d)) == 5:
            cnt += (d[0] + d[-1]) * 2 <= sum(d[1:-1]) * 3
    print(cnt)  # 2776

