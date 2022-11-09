import sys
def DFS(L):
    if L ==m:
        for j in res:
            print(j,end=' ')
        print()
    else:
        for i in range(n):
            res[L]=a[i]
            DFS(L+1)

n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
res = [0]*m
DFS(0)