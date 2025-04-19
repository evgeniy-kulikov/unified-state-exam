
# https://stepik.org/lesson/499908/step/11?unit=491458
with open('18-k3.txt') as fl:
    ls = list(map(int, fl))
res = 100_000
for i in range(len(ls) - 5):
    for k in range(i + 1, i + 6):
        sm = sum([ls[i], ls[k]])
        if not sm % 2:
            res = min(res, sm)
print(res) # 30




