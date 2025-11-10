

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
