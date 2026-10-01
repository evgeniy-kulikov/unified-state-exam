""""""
"""
Task 09
ЕГЭ Информатика 2027. Все задания 1-27
https://stepik.org/course/233165

task_09_100495
course_100495
"""

# https://stepik.org/lesson/564220/step/7?unit=558468
# очень быстро
from collections import Counter
d = [[*map(int, i.split())] for i in open('add/course_100495/9-228.txt')]
cnt = [[Counter(i)] for i in zip(*d)]
c = 0
for row in range(len(d)):
    for n in range(6):
        if d[row].count(d[row][n]) == 1:
            if cnt[n][0][d[row][n]] > 180:
                c += 1
print(c)  # 46324
# очень долго
d = [[*map(int, i.split())] for i in open('add/course_100495/9-228.txt')]
for i in range(len(d)):
    for n in range(6):
        if d[i].count(d[i][n]) == 1:
            c = 0
            for r in range(len(d)):
                if d[r][n] == d[i][n]:
                    c += 1
            if c > 180:
                cnt += 1
print(cnt)  # 46324


# https://stepik.org/lesson/564220/step/11?unit=558468
d = [[*map(int, i.split())] for i in open('09.txt')]
cnt = 0
for n in d:
    mx = max(n)
    cnt_mx = n.count(mx)
    if cnt_mx in (3, 4):
        if len(set(n)) == 9 - cnt_mx:
            n1 = sorted(i for i in n if n.count(i)==1)
            cnt += n1[0] + n1[-1] <= sum(n1[1:-1])
print(cnt)  # 213


# https://stepik.org/lesson/564220/step/12?unit=558468
d = [[*map(int, i.split())] for i in open('09.txt')]
for n in d:
    n1 = [i for i in n if n.count(i)==1]
    n2 = [i for i in n if n.count(i)==2]
    n3 = [i for i in n if n.count(i)==3]
    if len(n2 + n3) == 5:
        if n1[0] <= min(n2 + n3):
            res = min(n2 + n3)
print(abs(res))  # 26


