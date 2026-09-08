

# https://stepik.org/lesson/687436/step/6?unit=686601
# Сколько различных чётных чисел, меньших 100, можно получить из исходного числа 3?
def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+3, b) + f(a*3, b)

cnt = 0
for n in range(4, 100, 2):
    if f(3, n):
        cnt += 1
print(cnt)  # 16


