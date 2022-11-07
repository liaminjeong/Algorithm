import sys
def DFS(L):
    if L == m:
        for j in res:
            print(j,end=' ')
        print()
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i]=1
                res[L] = a[i]
                DFS(L+1)
                ch[i]=0

n,m =map(int,input().split())
a = list(map(int,input().split()))
a.sort()
res=[0]*m
ch=[0]*(n+1)
DFS(0)