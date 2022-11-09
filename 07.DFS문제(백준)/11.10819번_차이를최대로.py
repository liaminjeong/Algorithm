import sys

def DFS(L):
    global res
    if L ==n:
        sum=0
        for j in range(n-1):
            sum += abs(p[j]-p[j+1])  
        if res <sum:
            res = sum
    else:
        for i in range(n):
            if ch[i] ==0:
                ch[i]=1
                p[L] = a[i]
                DFS(L+1)
                ch[i]=0
            
n = int(input())
a = list(map(int,input().split()))
p = [0]*n
ch = [0]*(n+1)
res = -2147000000
DFS(0)
print(res)















# input 
# 6
# 20 1 15 8 4 10

# output
# 62
