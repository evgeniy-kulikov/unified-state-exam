""""""
"""
course_72713
task_14_72713
task 14
https://stepik.org/course/72713/syllabus
Подготовка к ЕГЭ по информатике
"""


# https://stepik.org/lesson/410146/step/6?unit=399518
n = 2*729**333 + 2*243**334 - 81**335 + 2*27**336 - 2*9**337 - 338
cnt = 0
while n:
    cnt += bool(n % 9)
    n //= 9
print(cnt)  # 149 4 0 0 2 0 0


# https://stepik.org/lesson/410146/step/6?unit=399518
n = 2*729**333 + 2*243**334 - 81**335 + 2*27**336 - 2*9**337 - 338
cnt = 0
while n:
    cnt += bool(n % 9)
    n //= 9
print(cnt)  # 149 4 0 0 2 0 0


# https://stepik.org/lesson/410146/step/9?unit=399518
n = 4**34 + 5*4**22 + 4**13 + 2*4**9 + 82
c = [0] * 16
while n:
    c[n % 16] += 1
    n //= 16
print(16 - c.count(0))  # 6



