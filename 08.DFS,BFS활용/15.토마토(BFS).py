import sys
sys.setrecursionlimit(10**6)
from collections import deque

dx = [-1,0,1,0] 
dy = [0,1,0,-1]

#n : 상자의 세로
#m : 상자의 가로
n,m = map(int,sys.stdin.readline().split())

# 1:익토, 0:익지않은토, -1:토마토없음
box = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
dis = [[0]*n for _ in range(m)]
Q = deque()

for i in range(m):
    for j in range(n):
        if box[i][j] == 1:
            Q.append((i,j)) #시작점 append
            dis[i][j] = 0   #익는데 걸리는 날짜

while Q:
    tmp = Q.popleft()
    #print('tmp[0]: ',tmp[0],'tmp[1]: ',tmp[1],end=' ')
    for p in range(4):
        a = tmp[0]+dx[p]
        b = tmp[1]+dy[p]

        if 0<=a<m and 0<=b<n and box[a][b]==0: #ch[a][b]==0:
            box[a][b] = 1
            dis[a][b] = dis[tmp[0]][tmp[1]] + 1
            Q.append((a,b))
#flag 가 '1'이면 위의 코드 수행
#flag 가 '0'이면 익지못하는 상황
flag = 1 

for i in range(m):
    for j in range(n):
        if box[i][j] == 0:
            flag =0 #익지못하는상황

if flag ==1:
    print(max(map(max,dis))) #2차원배열에서 max값 구하는방법
elif flag==0:#익지못하는상황
    print(-1)
else:
    print(0)
            





