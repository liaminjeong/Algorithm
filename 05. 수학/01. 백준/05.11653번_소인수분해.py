import sys
n = int(input())

factor = 2
factors = []

while factor**2 <=n:
    while n%factor ==0:
        n = n//factor
        factors.append(factor)
    factor+=1

if n>1:
    factors.append(n)
factors.sort()
for i in factors:
    print(i)


