""""""
"""
Task 15
Информатика Подготовка к ЕГЭ 2026
https://stepik.org/course/182932
Задачи на отрезки, множества и пр.
"""


""" 1.3 Повторение 3 часть """
# https://stepik.org/lesson/1342070/step/6?unit=1357751
def f(x):
    # return ((x in {a}) <= (not (x in p))) and ((not (x in q)) <= (not (x in {a})))
    # return (not (x in {a}) or not (x in p)) and (x in q or not (x in {a}))
    return not (x in {a}) or (not (x in p)) and (x in q)


p = {i for i in range(1, 20, 2)}
q = {i for i in range(2, 30, 3)}
res = set()

for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        res |= {a}
print(len(res))  # 7


# https://stepik.org/lesson/1342070/step/7?unit=1357751
def f(x,y):
    return ((a < x) or (x**2 - 7*x + 10 > 0)) and ((a >= y) or (y**2 + 7*y + 12 > 0))

res = set()
for a in range(-50, 50, 1):
    if all(f(x, y) for x in range(-500, 500, 1) for y in range(-500, 500, 1)):
        res |= {a}
print(len(res))  # 5
print(res)  # {0, 1, -1, -3, -2}


# https://stepik.org/lesson/1342070/step/8?unit=1357751
def f(x,y):
    return (x > 68 or y > 89) or (2*x - 7*y < a)

res = 10**6
for a in range(200):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        res = min(res, a)
print(res)  # 137


# https://stepik.org/lesson/1342070/step/9?unit=1357751
def f(x):
    return not (x & a) or (x & 168 or x & 69)

res = 0
for a in range(1, 500):
    if all(f(x) for x in range(1000)):
        res = max(res, a)
print(res)  # 237
