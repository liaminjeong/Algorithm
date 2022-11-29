import sys
from collections import deque
#시계방향
dx = [-1,0,1,0]
dy = [0,1,0,-1]
board = [list(map(int,input().split())) for _ in range(7)]
print(board)
dis = [[0]*7 for _ in range(7)]
Q = deque()
Q.append((0,0))
board[0][0]=1 #한번 방문한 곳은 벽(1)로 체크해버림

while Q:#큐가 비어있으면 멈춤
    tmp = Q.popleft() #Q에서 처음에 (0,0)좌표가 빠짐
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]

        #경계선밖의 좌표 금지 and board[x][y]가 통로일때
        if 0<=x<7 and 0<=y<7 and board[x][y]==0:
            board[x][y] = 1 #갔던 곳 재방문 하지 않게 1(벽)로 체크함, 체크효과
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            #dis[tmp[0]][tmp[1]] 첫지점
            Q.append((x,y))

if dis[6][6] ==0: #도착지점이 0이다 그럼 도착 못한거 
    print(-1) #도착할 수 없으면 -1
else: 
    print(dis[6][6])

    