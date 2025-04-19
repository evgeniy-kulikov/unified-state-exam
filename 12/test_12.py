# https://stepik.org/lesson/449926/step/1?auth=login&unit=440312
cnt = set()
for n in range(1, 1000):  # s = '8' тоже нужна )))
    s = '8' * n
    while '555' in s or '888' in s:
            s = s.replace('555', '8', 1)
            s = s.replace('888', '55', 1)
    cnt.add(s)
print(len(cnt))  # 8
print(cnt)  # {'88', '55', '5588', '558', '8', '85', '8588', '858'}


