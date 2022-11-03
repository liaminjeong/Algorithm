from re import A
import sys

n = int(input())

for i in range(n):
    m = int(sys.stdin.readline())

    ch =[0]*(m+1)
    fac = []
    for x in range(2,m+1):
        if ch[x]==0:
            fac.append(x)
        
        for j in range(x*2,m+1,x):
            ch[j]=1

    #fac 에 소수가 들어있음
   
    a = m//2 #중간부터 찾는다 why?차가 적은것을 출력해야하니까
    b = a 
    while a>0:
        if a in fac and b in fac:
            print(a,b)
            break
        else:
            a-=1
            b+=1