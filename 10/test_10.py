
# https://stepik.org/lesson/1401039/step/2?unit=1418001
import re
reg = r'(?i)\w*все\w+'
cnt = 0
with open('add/course_100138/10_2024.txt', encoding='utf-8') as fl:
    data = fl.read()
    d = re.findall(reg, data)
    for s in d:
        cnt += 1
        print(cnt, s)
# 9

