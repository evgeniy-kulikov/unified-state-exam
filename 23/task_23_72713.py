""""""
"""
course_72713
task 23
https://stepik.org/course/72713/syllabus
Подготовка к ЕГЭ по информатике
"""



# https://stepik.org/lesson/1256931/step/1?unit=1270945
# слишком много программ
from functools import lru_cache
@lru_cache()
def f(a, b):
    if a > b:
        return 0
    if a==b:
        return 1
    return f(a+1, b) + f(a+2, b)
print(f(1,50))  # 12586269025

# Динамический подход
# 0-й индекс не используется. 1-й и 2-й индекс - это исходное число (по кол-ву команд)
# с 3-го индекса и далее - число программ для конечного числа
f = [1] * 51
for i in range(3,len(f)):
    f[i] = f[i-1] + f[i-2]
print(f[50])  # 12586269025



# https://stepik.org/lesson/1256931/step/2?unit=1270945
# слишком много программ
from functools import lru_cache
@lru_cache()
def f(a, b):
    if a > b:
        return 0
    if a==b:
        return 1
    return f(a+1, b) + f(a+3, b)
print(f(2,60))  # 2598919345

# Динамический подход (первые индексы считаем руками)
f=[2]*61  # в 5-ку попадаем 2-мя путями
f[3]=1  # в 3-ку попадаем 1-м путем
f[4]=1  # в 4-ку попадаем 1-м путем
for i in range(6,len(f)):
    f[i]=f[i-1]+f[i-3]
print(f[60])  # 2598919345


# https://stepik.org/lesson/1256931/step/8?unit=1270945
from sys import setrecursionlimit
from functools import lru_cache
setrecursionlimit(10000)  # ❗❗❗ Иначе Stepik не примет решение

@lru_cache(maxsize=None)
def f(a, b, c=0):
    c += a==13
    if a > b or a==29:
        return 0
    if a==b and c:
        return 1
    return f(a+1, b, c) + f(a*2, b, c) + f(a*3, b, c)
print(f(2,639))



