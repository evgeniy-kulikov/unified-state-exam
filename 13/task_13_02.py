""""""
"""
Task 13
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""

# https://stepik.org/lesson/1086799/step/5?auth=login&unit=1097283
# !!!  НЕ РЕШЕНО  !!!
"""
11111 000   248  маска
10100 000   160  узел 1
10101 111   175  узел 2
"""
# from ipaddress import ip_network, ip_address
# ip1 = ip_address('191.131.175.201')
# ip2 = ip_address('191.131.160.170')
# for n in range(17, 33):
#     try:
#         net_1 =  ip_network(f'{ip1}/{n}')
#         net_2 =  ip_network(f'{ip2}/{n}')
#         if net_1 != net_2:
#             print(net_1, net_2, sep='\n')
#             print(n)
#             print(bin(n))
#     except:
#         pass


# https://stepik.org/lesson/1086799/step/8?auth=login&unit=1097283
# НЕ ПОНЯЛ !!!
from ipaddress import ip_network
res = 0
for mask in range(17, 25):
    try:
        cnt = 0
        for i in ip_network(f'115.53.128.0/{mask}'):
            # print(i)
            cnt += 1
        if cnt > 1000:
            res += 1
    except:
        pass
print(res)  # 6


# https://stepik.org/lesson/1086799/step/1?auth=login&unit=1097283
from ipaddress import *

cnt = 0
net = ip_network(f'192.168.32.160/28')
for i in net:
    if not bin(int(i))[2:].count('1') % 2:
        cnt += 1
        print(bin(int(i))[2:])
print(cnt) # 8

# вариант
# в первых 3-х октетах и в половинке последнего (в адресе сети) кол-во единиц 8 (четное)
# Ищем четность единиц в последней половинке октета
cnt = 0
for  i in range(240, 256):
    if not bin(i)[2:].count('1') % 2:
        cnt += 1
print(cnt) # 8

# https://stepik.org/lesson/1086799/step/2?auth=login&unit=1097283
# адрес сети (000 0000) и широковещательный (111 1111) не используем
cnt = 0
for  i in range(129, 255):
    cnt += 1
print(cnt) # 126
# короче  255 - 129 = 126


# https://stepik.org/lesson/1086799/step/3?auth=login&unit=1097283
"""
Решение руками (рассматриваем 3-й октет):
00111000 - 56  сеть  (248.228.56.0)
11111000 - 248 маска (255.255.248.0)
00111100 - 60  узел  (248.228.60.240)
"""
from ipaddress import ip_network
for n in range(17, 25):  # 16 единиц уже есть в первых 2-х октетах маски
    try:
        for i in ip_network(f'248.228.56.0/{n}', strict=True):
            if str(i) == '248.228.60.240':
                # print(n - 16)  # 5 единиц в 3-м октете маски
                b = '1' * (n - 16) + '0' * (8 - (n - 16))
                print(b)  # 11111000
                print(int(b, 2))  # 248
    except:
        pass


# https://stepik.org/lesson/1086799/step/4?auth=login&unit=1097283
"""
Решение руками (рассматриваем 3-й октет):
11000000 - 192  сеть  (111.81.192.0)
11000000 - 192 маска (255.255.192.0)
11010000 - 208  узел  (111.81.208.27)
"""
from ipaddress import ip_network
for n in range(17, 25):  # 16 единиц уже есть в первых 2-х октетах маски
    try:
        for i in ip_network(f'111.81.192.0/{n}', strict=True):
            if str(i) == '111.81.208.27':
                # print(n - 16)  # 2 единицы  3-м октете маски
                b = '1' * (n - 16) + '0' * (8 - (n - 16))
                print(b)  # 11000000
                print(int(b, 2))  # 192
    except:
        pass


# https://stepik.org/lesson/1086799/step/5?auth=login&unit=1097283
from ipaddress import ip_network
cnt = 0
for i in ip_network('202.75.38.152/255.255.255.248'):
    if '111' in bin(int(i)):
        print(str(i))
        cnt += 1
print(cnt)  # 4


# https://stepik.org/lesson/1086799/step/6?unit=1097283
from ipaddress import *
for n in range(17, 25):
    net1 = ip_network(f'191.131.175.201/{n}', 0)
    net2 = ip_network(f'191.131.160.170/{n}', 0)
    if net1 != net2:
        s = '1' * (n - 16)
        print(int(s.ljust(8, '0'), 2))  # 248
        break


# https://stepik.org/lesson/1086799/step/7?auth=login&unit=1097283
from ipaddress import ip_network
cnt = 0
for el in ip_network('99.64.0.0/10'):
    if bin(int(el))[-2:] == '11':
        cnt += 1
print(cnt)  # 1048576


# https://stepik.org/lesson/1086799/step/8?unit=1097283
from ipaddress import *
cnt = 0
for n in range(17, 25):
    net = ip_network(f'115.53.128.88/{n}', 0).hosts()
    cnt += len(list(net)) >= 1000
print(cnt) # 6


# https://stepik.org/lesson/1086799/step/9?unit=1097283
from ipaddress import *
cnt = 0
net = ip_network('216.130.64.0/255.255.192.0', 0)
for el in net.hosts():
    n = str(el).split('.')
    if all([not int(n[-2]) % 2, not int(n[-1]) % 2]):
        cnt += 1
print(cnt)  # 4095


# https://stepik.org/lesson/1086799/step/10?unit=1097283
from ipaddress import *
cnt = 0
net = ip_network('192.168.32.160/255.255.255.240', 0)
for el in net:
    cnt += f'{el:b}'.count('0') > 21
print(cnt)  # 11


# https://stepik.org/lesson/1086799/step/11?unit=1097283
from ipaddress import *
for n in range(17, 25):
    net = ip_network(f'158.198.228.220/{n}', 0)
    if str(net.network_address) == '158.198.128.0':
        s = ('1' * (n - 16)).ljust(8, '0')
        print(int(s, 2))  # 128
        # print(n)  # 17


# https://stepik.org/lesson/1086799/step/12?unit=1097283
from ipaddress import *
cnt = 0
net = ip_network('213.0.0.0/255.192.0.0')
for n in net:
    cnt  += '111' in f'{n:b}'
print(cnt)  # 3438828


# https://stepik.org/lesson/1086799/step/13?unit=1097283
from ipaddress import *
for a in range(255, -1, -1):
    net = ip_network(f'159.242.{a}.223/255.255.254.0', 0)
    ls_net = list(net.hosts())
    ls_net.append(net.broadcast_address)  # hosts() не содержит широковещательный и сам адрес сети
    ls_net.append(net.network_address)

    if all(f'{i:b}'[:16].count('0') < f'{i:b}'[16:].count('0') for i in ls_net):
        print(a)  # 129
        break



