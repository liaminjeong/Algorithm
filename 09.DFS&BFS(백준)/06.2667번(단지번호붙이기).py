import sys
# sys.setrecursionlimit(10**6)
# #DFS
# def DFS(x,y):
#     global cnt
#     cnt+=1
#     home[x][y] = 0
#     for p in range(4):
#         a = x+dx[p]
#         b = y+dy[p]
#         if 0<=a<n and 0<=b<n and home[a][b] ==1:
#             DFS(a,b)
    
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# n = int(input())
# res = []
# home = [list(map(int,input().strip())) for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         if home[i][j] ==1:
#             cnt = 0
#             DFS(i,j)
#             res.append(cnt)

# print(len(res))
# res.sort()
# for x in res:
#     print(x)

#BFS
from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(input())
res = []
Q = deque()
home = [list(map(int,input().strip())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if home[i][j] == 1:
            cnt =1
            home[i][j] = 0
            Q.append((i,j))

            while Q:
                tmp = Q.popleft()
                for p in range(4):
                    a = tmp[0] + dx[p]
                    b = tmp[1] + dy[p]
                    if 0<=a<n and 0<=b<n and home[a][b]==1:
                        cnt+=1
                        home[a][b] = 0
                        Q.append((a,b))
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)
