"""
n=int(input())
if n==1 or (n>20 and (n%10)==1) and (n%100)!=11:
    print(n,'программист')
elif (n>1 and n<5) or (n>20 and (n%10)>1 and (n%10)<5):
    print(n,'программиста')
elif n==0 or (n> 1 and n<20) o
"""
def f(n):
    if str(n)[-1] == '1' and n != 11:
        return f'{n} копеека'
    if (1 < n < 5) or (n > 20 and str(n)[-1] in '234'):
        return f'{n} копейки'
    return f'{n} копеек'

# n = int(input())
for n in range(101):
    print(f(n))
