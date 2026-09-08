""""""
"""
course_72713
task_14_72713
task 14
https://stepik.org/course/72713/syllabus
Подготовка к ЕГЭ по информатике
"""


# https://stepik.org/lesson/1340034/step/15?unit=1356035
n = 2*729**333 + 2*243**334 - 81**335 + 2*27**336 - 2*9**337 - 338
cnt = 0
while n:
    cnt += bool(n % 9)
    n //= 9
print(cnt)



