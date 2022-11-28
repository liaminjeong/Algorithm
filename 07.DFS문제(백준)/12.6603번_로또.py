import sys
def DFS(L,s):
    global res
    if L == k:
        for j in res:
            print(j,end=' ')
        print()
    else:
        for i in range(s,k):
            res[L] = kL[i]
            DFS(L+1,i+1)


tmp = list(map(int,input().split()))
k = tmp[0]
kL = tmp[1:]
res = [0]*k
DFS(0,0)
