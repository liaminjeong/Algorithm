import sys
sys.setrecursionlimit(10**6)

#DFS
# def DFS(H,x,y):
#     ch[x][y] = 1
#     for p in range(4):
#         a = x+dx[p]
#         b = y+dy[p]
#         if 0<=a<n and 0<=b<n and ch[a][b]==0 and land[a][b]>H:
#             DFS(H,a,b)

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# n = int(input())
# land = [list(map(int,input().split())) for _ in range(n)]
# cnt = 0
# res = 0
# for h in range(100):
#     ch = [[0]*n for _ in range(n)] #새롭게 한바퀴 돌때마다 초기화 해줌 
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if ch[i][j]==0 and land[i][j]>h:
#                 cnt+=1
#                 DFS(h,i,j)
#     res = max(res,cnt)
#     if cnt==0:
#         break
# print(res)

#BFS
from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(input())
land = [list(map(int,input().split())) for _ in range(n)]
Q = deque()
res = 0
cnt = 0
for h in range(100):
    ch = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if ch[i][j]==0 and land[i][j]>h:
                Q.append((i,j))
                ch[i][j] = 1
                cnt+=1
                while Q:
                    tmp = Q.popleft()
                    for p in range(4):
                        a = tmp[0]+dx[p]
                        b = tmp[1]+dy[p]
                        if 0<=a<n and 0<=b<n and ch[a][b]==0 and land[a][b]>h:
                            ch[a][b]=1
                            Q.append((a,b))
    
    res = max(res,cnt)
    if cnt ==0:
        break
print(res)

