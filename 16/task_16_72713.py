""""""
"""
task 16
https://stepik.org/course/72713/syllabus
Подготовка к ЕГЭ по информатике
"""

# https://stepik.org/lesson/1112770/step/2?unit=1126139
def f(n):
    if not n:
        return 0
    if n % 2:
        return 1 + f(n - 1)
    return f(n // 2)

for n in range(10000):
    if f(n) == 12:
        print(n)  # 4095
        break


# https://stepik.org/lesson/1112770/step/9?unit=1126139
def f(n):
    if n == 1:
        return 1
    return f(n - 1) - g(n - 1)

def g(n):
    if n == 1:
        return 1
    return f(n - 1) + g(n - 1)

print(f(15) // g(15))  # -1


