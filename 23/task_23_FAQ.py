

# https://stepik.org/lesson/1149683/step/4?unit=1161670
# Сколько существует программ которые число 3 преобразуют в 20
# и при этом траектория вычислений содержит число 9 и 12
def f(st, end):
    if st == end:
        return 1
    if st > end:
        return 0
    return f(st + 1, end) + f(st + 3, end) + f(st * 2, end)

print(f(3, 9) * f(9, 12) * f(12, 20))  # 234




# https://stepik.org/lesson/1149683/step/9?unit=1161670
# Определите число, для получения которого из числа 31 существует 1001 программа
def f(st, end):
    if st == end:
        return 1
    if st > end:
        return 0
    return f(st + 2, end) + f(st + 4, end) + f(st + 5, end)

for n in range(100):
    if f(31, n) == 1001:
        print(n)  # 56
        break




# https://stepik.org/lesson/1256931/step/1?unit=1270945
# Сколько существует программ, для которых при исходном числе 1 результатом является число 50?
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

# Динамический подход (начальные индексы считаем руками)
# 0-й индекс не используется.
# в 1-цу ведет 1 путь (старт), в 2-ку ведет 1 путь
f = [1] * 51
for i in range(3,len(f)):
    f[i] = f[i-1] + f[i-2]
print(f[50])  # 12586269025