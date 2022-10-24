import sys
n = int(input())

def factorize(n):
    factor = 2
    factors = []
    while(factor**2 <= n):
        print('factor**2 ::: ' , factor**2)
        while(n%factor == 0):
            n = n//factor
            factors.append(factor)
        factor +=1
        print(factor)
    if (n>1):
        factors.append(n)
    return factors

print(factorize(n))