import sys
sys.setrecursionlimit(10**6)
#DFS로 실패
# def DFS(v):
#     global cnt
#     print('v : ',v)
#     if v == 3:
#         return
#     else:
#         for i in range(1,n+1):
#             print('dong[v][i]: ',dong[v][i],'v: ',v,'i: ',i,end= ' ')
#             print()
#             if dong[v][i]==1 and ch[i]==0:
#                 print('들어올때만 들어와')
#                 cnt+=1
#                 ch[i] = 1
#                 DFS(i)
#                 ch[i] =0
# n = int(input())
# m = int(input())
# dong = [[0]*(n+1) for _ in range(n+1)]
# ch = [0]*(n+1)
# cnt = 0
# for i in range(m):
#     a,b = map(int,input().split())
#     dong[a][b] = 1
#     dong[b][a] = 1

# for x in dong:
#     print(x)
# ch[1] = 1
# DFS(1)
# print(cnt)

from collections import deque

n = int(input())
m = int(input())
dong = [[0]*(n+1) for _ in range(n+1)]
ch = [0]*(n+1)
cnt = 0
for i in range(m):
    a,b = map(int,input().split())
    dong[a][b] = 1
    dong[b][a] = 1

Q = deque()
Q.append((1,0)) #내 학번, 관계깊이
ch[1]=1

while Q:
    tmp = Q.popleft()
    if tmp[1] == 2:
        break
    for i in range(1,n+1):
       if dong[tmp[0]][i] ==1 and ch[i] ==0:
            ch[i] = 1
            Q.append((i,tmp[1]+1))
            cnt+=1
print(cnt)



    
      


