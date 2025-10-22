""""""
"""
Task 17
Подборка задач для подготовки к ЕГЭ по информатике 2026 | itpy
https://stepik.org/course/122969
"""

# https://stepik.org/lesson/1343760/step/1?unit=1359470
cnt = 0
MX = 0
with open('add/course_122969/17_1.txt') as file:
    d = list(map(int, file))
    mn = min(i for i in d if not i % 19)
    for i in range(len(d) - 1):
        if any(k for k in d[i:i+2] if not k % mn):
            cnt += 1
            MX = max(MX, sum(d[i:i+2]))
    print(cnt, MX)  # 142 175430


# https://stepik.org/lesson/1343760/step/2?unit=1359470
cnt = 0
MX = 0
with open('add/course_122969/17_2.txt') as file:
    d = list(map(int, file))
    mn = max(i for i in d if abs(i) % 10 == 3 and len(str(abs(i))) == 5)
    for i in range(len(d) - 2):
        if any(k for k in d[i:i+3] if str(k)[-1] == '3'):
            if sum(d[i:i+3]) <= mn:
                cnt += 1
                MX = max(MX, sum(d[i:i+3]))
    print(cnt, MX)  # 1767 99081







