""""""
"""
# Рекурсия
# Подготовка к ЕГЭ информатика
# https://stepik.org/course/57248
"""

# https://stepik.org/lesson/297866/step/1?unit=279630
def f(n):
    if n > 1:
        return f(n - 1) + g(n - 1)
    return n + 1

def g(n):
    if n > 1:
        return g(n - 1) + f(n)
    return n - 1
print(f(5))  # 26


# https://stepik.org/lesson/297866/step/2?unit=279630
def f(n):
    if n > 3:
        print(n, end='')
        f(n // 3)
        n += 1
        f(n - 3)
    else:
        print(n, end='')
print(f(9))  # 9372513


# https://stepik.org/lesson/297866/step/3?unit=279630
def f(n):
    n -= 1
    if n > 2:
        print(n, end='')
        f(n - 1)
        g(n - 2)
    else:
        print(n + 2, end='')

def g(n):
    print(n, end='')
    if n > 2:
        n -= 1
        g(n - 1)
        f(n - 2)
    else:
        print(n + 1, end='')
print(f(6))  # 533123121


# https://stepik.org/lesson/297866/step/4?unit=279630
def f(n):
    if n > 0:
        f(n - 4)
        f(n // 3)
        print(n, end="")
print(f(9))  # 115139


# https://stepik.org/lesson/297866/step/5?unit=279630
def f(n):
    if n > 0:
        f(n - 1)
        print(n, end='')
        f(n // 4)
print(f(5))  # 1234151

# https://stepik.org/lesson/297869/step/1?unit=279634
def f(n):
    if n > 3:
        print(n, end='')
        f(n // 3)
        n += 1
        f(n - 3)
    else:
        print(n, end='')
print(f(9))  # 9372513


# https://stepik.org/lesson/454791/step/1?unit=445218
def f(n):
    if n > 25:
        return n * n + 4 * n + 3
    if n <= 25 and not n % 3:
        return f(n + 1) + 2 * f(n + 4)
    if n <= 25 and n % 3:
        return f(n + 2) + 3 * f(n + 5)
cnt = 0
for n in range(1, 1001):
    cnt += sum(map(int, str(f(n)))) == 24
print(cnt)  # 100


# https://stepik.org/lesson/454791/step/2?unit=445218
def f(n):
    if n <= 15:
        return n * n + 3 * n + 9
    if n > 15 and not n % 3:
        return f(n - 1) + n - 2
    if n > 15 and n % 3:
        return f(n - 2) + n + 2
cnt = 0
for n in range(1, 1001):
    cnt += not len(list(filter(lambda x: x in '13579', str(f(n)))))
print(cnt)  # 33


# https://stepik.org/lesson/454791/step/3?unit=445218
def f(n):
    if n <= 15:
        return 2 * n * n + 4 * n + 3
    if n > 15 and not n % 3:
        return f(n - 1) + n * n + 3
    if n > 15 and n % 3:
        return f(n - 2) + n - 6
cnt = 0
for n in range(1, 1001):
    cnt += not len(list(filter(lambda x: x in '02468', str(f(n)))))
print(cnt)  # 27


# https://stepik.org/lesson/454791/step/4?unit=445218
def f(n):
    if n <= 18:
        return n + 3
    if n > 18 and not n % 3:
        return (n // 3) * f(n // 3) + n - 12
    if n > 18 and n % 3:
        return f(n - 1) + n * n + 5
cnt = 0
for n in range(1, 1001):
    cnt += not len(list(filter(lambda x: x in '13579', str(f(n)))))
print(cnt)  # 16


# https://stepik.org/lesson/454791/step/5?unit=445218
def f(n, m):
    if not m:
        return n
    return f(m, n % m)
cnt = set()
for n in range(100, 1001):
    for m in range(100, 1001):
        if f(n, m) == 30:
            cnt.add(n)
print(len(cnt))  # 30


# https://stepik.org/lesson/454791/step/6?unit=445218
def f(n):
    global res
    res += (n + 1)
    if n > 1:
        res += (2 * n)
        f(n - 1)
        f(n - 3)

res = None
for n in range(1, 50):
    res = 0
    f(n)
    if res > 10 ** 6:
        print(n, res)  # 30 1249317  -->  301249317
        break


# https://stepik.org/lesson/454791/step/7?unit=445218
# from functools import lru_cache
cnt = 0
# @lru_cache  #  Использование @lru_cache влияет на 'global cnt', что дает неверный ответ !!!
def f(n):
    global cnt
    cnt += 1
    if n >= 1:
        cnt += 1
        f(n - 1)
        f(n - 3)
        cnt += 1
f(40)
print(cnt)  # 22947841


# https://stepik.org/lesson/454791/step/8?unit=445218
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * f(n - 1) + g(n - 1) - 2

def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) + 2 * g(n - 1)
print(f(14) + g(14))  # 1594324


# https://stepik.org/lesson/454791/step/9?unit=445218
def f(n):
    if not n:
        return 3
    if 0 < n <= 15:
        return f(n - 1)
    if 15 < n < 100:
        return 2.5 * f(n - 3)
    if n >= 100:
        return 3.3 * f(n - 2)
print(f(100))  # 1373900992973.631  --> 6


# https://stepik.org/lesson/454791/step/10?unit=445218
def f(n):
    if n <= 1:
        return 1
    if n > 1 and not n % 2:
        return 11 * n + f(n - 1)
    return 11 * f(n - 2) + n

res = 0
for n in range(35, 51):
    num = f(n)
    if not num % 2:
        res += num
print(len(str(res)))  # 25


# https://stepik.org/lesson/454791/step/11?unit=445218
def f(n):
    if n <= 1:
        return 1
    if n > 1 and not n % 3:
        return 2 * f(n - 1) + f(n - 2)
    return 3 * f(n - 2) + f(n - 1)

def prime(n):  # нахождение простого числа
    if n in [1, 2]:
        return True
    if not n % 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if not n % i:
            return False
    return Truee

cnt = 0
for n in range(1, 36):
    num = sum(map(int, str(f(n))))
    cnt += prime(num)
print(cnt)  # 2


# https://stepik.org/lesson/454791/step/12?unit=445218
from functools import lru_cache

def prime(n):  # нахождение простого числа
    if n in [1, 2]:
        return True
    if not n % 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if not n % i:
            return False
    return True

@lru_cache
def f(n):
    if n == 0:
        return 1
    if n > 0:
        return 7 * (n - 1) + f(n - 1)

cnt = 0
for n in range(1, 201):
    num = f(n)
    cnt += prime(num)
print(cnt)  # 44


