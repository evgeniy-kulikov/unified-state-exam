""""""


# Тонкости разделения
s = 'NNNA'
s = s.replace('NN', 'N N')  #  N NNA   (неверно)

while 'NN' in s:
    s = s.replace('NN', 'N N')  #  N N NA   (верно)



""" Решения через сплит """
# split('Y')
# Макс. кол-во символов, среди которых не более "n" символов 'Y'
res = 0
n = 3  # кол-во Y
s = '1Y2Y3Y4Y55555'.split('Y')  # ['1', '2', '3', '4', '55555']
for i in range(len(s) - n):
    r = len(''.join(s[i:i + (n+1)])) + n
    res = max(res, r)
print(res)

# Макс. кол-во символов, среди которых ровно "n" символов 'AB'
res = 0
n = 3  # кол-во  'AB'
s = 'AB__AB_ABAB___AB____'.replace('AB', 'A B')
s = s.split()  # ['A', 'B__A', 'B_A', 'BA', 'B___A', 'B____']
for i in range(len(s) - n):
    # row = s[i:i + n+1]
    # res = max(res, len(''.join(row)))
    res = max(res, sum(map(len, s[i:i + n+1])))
print(res)


s = 'AXMM__AXMM__AXM_AXMM'.replace('AXMM', 'AXM XMM')
s = s.split()  # ['AXM', 'XMM__AXM', 'XMM__AXM_AXM', 'XMM']
res = max(s, key=len)
print(len(res))


"""
Текстовый файл состоит из символов K, L, M и N. Определите максимальное количество символов в непрерывной подпоследовательности, 
состоящей из идущих подряд групп символов KLMN в указанном порядке, 
при этом в начале и в конце искомой последовательности группа символов KLMN может быть неполной.
Искомая последовательность должна содержать не менее одной полной группы символов KLMN. 
Например, условию задачи удовлетворяют: MNKLMNKLMNK, или NKLMNKLMNKL, или KLMNKLMNKLM и т.п.
"""
MX = 0
cnt = 3

s = '__MNKLMNKLMNKL__KLM'
for i in range(len(s) - 3):
    if s[i:i + 4] in 'KLMNKLM':
        cnt += 1
        MX = max(MX, cnt)
    else:
        cnt = 3
print(MX)


""" Решения через цикл """
# Сдвиг левой границы
#  максимальное количество идущих подряд символов, среди которых ABC
# (в указанном порядке) встречается ровно 2 раза
MX = 0
cnt = 0
l = 0
s = '__ABC_ABC_ABC_'
for r in range(2, len(s)):
    if s[r-2:r+1] == 'ABC':
        cnt += 1
    while cnt > 2:
        if s[l:l+3] == 'ABC':
            cnt -= 1
        l += 1
    if cnt == 2:
        MX = max(MX, r - l + 1)
print(MX)  # 12

MX = 0
cnt = l = 0
# Максимальное кол-во символов, среди которых ровно 10 "Т"
s = '22' + 'T' + '333' + 'T'*10 + '5555'
for r in range(len(s)):
    pass
    cnt += s[r] == 'T'
    while cnt > 10:
        if s[l] == 'T':
            cnt -= 1
            pass
        l += 1
    if cnt == 10:
        MX = max(MX, r - l + 1)
        pass
print(MX)  # 18



# Двойной цикл
s = '1_22_333_4444_55555_6_7'
m = 0
for l in range(len(s)):
    for r in range(l + m, len(s) + 1):
        st = s[l:r]
        if st.count('_') > 3:
            break
        if st.count('_') == 3:
            m = max(m, len(st))
            pass
print(m) # 17  '22_333_4444_55555'





from re import *
a = r'[1-9]\d*|0'
reg = rf'{a}[+*-]{a}={a}'