import sys
from collections import deque

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
dx = [-1,-1,0,1,1,1,0,-1] #상하좌우 대각선 모두 검사해야하기 때문에
dy = [0,1,1,1,0,-1,-1,-1]
n = int(input())
cnt = 0
land = [list(map(int,input().split())) for _ in range(n)]
Q = deque()
for i in range(n):
    for j in range(n):
        if land[i][j] ==1: #처음 섬을 만나면 
            land[i][j] = 0
            Q.append((i,j))
            while Q:
                tmp = Q.popleft()
                for p in range(8): #상하좌우 대각선검사
                    a = tmp[0] + dx[p]
                    b = tmp[1] + dy[p]
                    #경계선벗어나면 안되고 섬일경우만 
                    if 0<=a<n and 0<=b<n and land[a][b]==1:
                        land[a][b] =0
                        Q.append((a,b))
            cnt+=1
            #처음에는 res 에 cnt를 넣어줬는데 
            #while문이 끝나면 하나의 섬을 검사한것임
            #하나의 섬을 발견할 때 cnt+1해줌 
            #여기서 하나의 섬이란 하나의 BFS가 끝났을때를 말함
print(cnt)
