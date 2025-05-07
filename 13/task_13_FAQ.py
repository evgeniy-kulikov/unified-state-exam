""""""

"""
хост (узел)  адрес комрьютера в сети
маска  - слева единицы, справа нули
адрес сети - количество нулей (двоичных) справа определяет количество узлов внутри сети


ip_address(address)
Take an IP string/int and return an object of the correct type.

ip_network(address, strict=True):
Take an IP string/int and return an object of the correct type.
ip_network('112.192.1.1', 0)    аргументы: [адрес хоста/сети],  [нестрогая проверка (ошибки игнорируются)]
Функция print() выводит сеть вместе с маской (кол-во единиц)
print( ip_network('64.128.194.208/255.255.240.0', 0))  # 64.128.192.0/20

Итерация по ip_network выдает объект, а не строку
net = ip_network('64.128.194.208/255.255.240.0', 0)
for n in net:
    a = str(n)       # 64.128.194.208
    b = int(n)       # 4656757
    c = f'{n}:b'     # 1001010110100101010101


ip_network(address).network_address
формирование IP адреса (маски в записи нет) в виде обЪекта (со строкой не сравнить)
str(ip_network(address).network_address)  формирование IP адреса в виде строки

ip_network(address).netmask
формирование адреса маски в виде обЪекта (со строкой не сравнить)

ip_network(address).hosts()
Generate Iterator over usable hosts in a network. 
it doesn't return the network or broadcast addresses

ip_network(address).num_addresses
Number of hosts in the current subnet
возвращает количество возможных номеров компьютеров в сети (включая адрес сети и широковешательный)

"""


"""
десятичное в двоичное
f'{8:b}'  -->  1000
bin(8)[2:]  -->  1000

двоичное в десятичное
int('1000', 2)  --> 8



'11'.ljust(8, '0')  -->  '11000000'

'11'.rjust(8, '0')  -->  '00000011'
'11'.zfill(8)  -->  '00000011'
"""

# конвертирование десятичного IP адреса в двоичный
def bin_ip(s: str):
    return '.'.join(f'{int(i):b}'.zfill(8) for i in s.split('.'))
