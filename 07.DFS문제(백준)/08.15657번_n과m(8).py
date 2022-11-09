import sys
def DFS(L,s):
    if L==m:
        for j in res:
            print(j,end=' ')
        print()
    else:
        for i in range(s,n):
            res[L] = a[i]
            DFS(L+1,i)

n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
res=[0]*m
DFS(0,0)