import sys
from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
n,m = map(int,input().split())
board = [list(map(int,input().strip())) for _ in range(n)]
dis = [[0]*m for _ in range(n)]
Q = deque()
Q.append((0,0))
dis[1][1] = 1

while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        # print('x: ',x,'y: ',y,end=' ')
        # print()
        if 0<=x<n and 0<=y<m and board[x][y]==1:
            board[x][y] = 0
            dis[x][y] = dis[tmp[0]][tmp[1]] +1
            Q.append((x,y))
            print(dis)
print(dis[n-1][m-1])