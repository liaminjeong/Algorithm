import sys
from collections import deque
sys.setrecursionlimit(10**6)

n = int(input())
m = int(input())
g = [[0]*(n+1) for _ in range(n+1)]
ch = [0]*(n+1)
cnt = 0
for i in range(1,m+1):
    a,b = map(int,input().split())
    g[a][b] = 1
    g[b][a] = 1

Q = deque()
Q.append(1)
ch[1] = 1
while Q:
    tmp = Q.popleft()
    for i in range(1,n+1):
        if g[tmp][i]==1 and ch[i]==0:
            ch[i] = 1
            Q.append(i)
            cnt+=1
print(cnt)

