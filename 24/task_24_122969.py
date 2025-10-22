""""""
"""
Task 24
Подборка задач для подготовки к ЕГЭ по информатике 2026 | itpy
https://stepik.org/course/122969
"""

MX = 0
with open('add/course_122969/24_11.txt') as file:
    s = file.read().strip()
    for l in range(len(s) - 1):
        cnt = 1
        for r in range(l, len(s)):
            row = s[l:r + 2]
            if row[-2].isdigit() == row[-1].isalpha():
                cnt += 1
                MX = max(MX, cnt)
            else:
                break
print(MX)  # 22


