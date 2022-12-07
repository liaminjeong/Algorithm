import sys
from collections import deque
sys.setrecursionlimit(10**6)

def DFS(v):
    ch[v]=1
    print(v,end =' ')
    for i in range(1,n+1):
        if g[v][i]==1 and ch[i]==0:
            DFS(i)
        
n,m,v = map(int,input().split())
g = [[0]*(n+1) for _ in range(n+1)]
ch = [0]*(n+1)
ch2 =[0]*(n+1)

for i in range(1,m+1):
    a,b = map(int,input().split())
    g[a][b] = 1
    g[b][a] = 1
DFS(v)

print()

#BFS
res2 = []
Q = deque()
Q.append(v)
ch2[v] = 1
while Q:
    now = Q.popleft()
    print(now,end=' ')
    for i in range(1,n+1):
        if g[now][i] ==1 and ch2[i]==0:
            ch2[i] = 1
            Q.append(i)
