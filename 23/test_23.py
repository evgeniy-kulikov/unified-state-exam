# https://stepik.org/lesson/460368/step/8?auth=login&unit=450951
def rep(n: int):
    # хитрое преобразование числа !!!
    s = ''
    for i in str(n):
        if i != '9':  s += str(int(i) + 1)
        else: s += i
    return int(s)

def f(st, en):
    if st > en: return 0
    if st == en: return 1
    return f(st + 1, en) + f(rep(st), en)
print(f(25, 51))  # 33
