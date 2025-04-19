
# https://stepik.org/lesson/1670114/step/7?unit=1693136
from math import dist

def centroid(cl):
    res = []
    for i in cl:
        res.append((sum(dist(i, j) for j in cl), i))
    return min(res)[1]

with open('27-10b.txt') as fl:
    data = [tuple(map(float, i.replace(',', '.').split())) for i in fl]
    clasters = [[] for _ in range(3)]
    for i in data:
        if i[1] > 0.5:
            clasters[0].append(i)
        elif i[0] > 2:
            clasters[1].append(i)
        else:
            clasters[2].append(i)

res = [centroid(i) for i in clasters]
cx = int(sum(i[0] for i in res) / 3 * 10_000)
cy = int(sum(i[1] for i in res) / 3 * 10_000)
print(cx, cy)
# 7881 -5340
