import sys
from collections import deque
sys.setrecursionlimit(10**6)

n,k = map(int,input().split())
max = 10**5
ch = [0]*(max+1)
Q = deque()
Q.append((n,0))
ch[n] =1
while Q:
    tmp = Q.popleft()
    if tmp[0] == k:
        print(tmp[1])
        break
    for i in (tmp[0]-1, tmp[0]+1, tmp[0]*2):
        if 0<=i<=max and ch[i]==0:
            ch[i]=1
            Q.append((i,tmp[1]+1))


