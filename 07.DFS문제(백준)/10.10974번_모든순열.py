import sys
def DFS(L):
    if L==n:
        for j in res:
            print(j,end=' ')
        print()
    else:
        for i in range(1,n+1):
            if ch[i] == 0:
                ch[i]=1
                res[L] = i
                DFS(L+1)
                ch[i]=0

n = int(input())
ch=[0]*(n+1)
res=[0]*n
DFS(0)