# https://stepik.org/lesson/1167509/step/9?unit=1179830
from fnmatch import fnmatch
def dv(n):
    d = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n // i}
    res = [i for i in d if not i % 2]
    if len(res) >= 4:
        return sum(res)

cnt = 7
for n in range(65000, 10**8):
    if fnmatch(str(n), '6*97*5?'):
        if dv(n):
            print(n, dv(n))
            cnt -= 1
    if not cnt:
        break
"""
69750 129792
69752 122080
69756 139536
69758 75152
609750 1103232
609752 1291248
609754 630840
"""
