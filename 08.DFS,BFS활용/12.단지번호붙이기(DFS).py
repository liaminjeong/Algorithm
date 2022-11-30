import sys
#BFS
from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
res = []
n = int(input())
home = [list(map(int,input())) for _ in range(n)]
Q = deque()
for i in range(n):
    for j in range(n):
        if home[i][j] ==1: #처음 1을 만난 곳에서 시작
            cnt = 1 #1을 만났으니 cnt =1로 초기화
            home[i][j] = 0 #방문한 곳 체크
            Q.append((i,j)) #처음 시작좌표를 Q에 append

            while Q: #Q가 비어있을때까지 돈다
                tmp = Q.popleft()
                for p in range(4): #4방향 체크
                    a = tmp[0] + dx[p]
                    b = tmp[1] + dy[p]
                    if 0<=a<n and 0<=b<n and home[a][b]==1:
                        cnt+=1 #좌표가 유효한 범위 안에 있고 1을 만나면 cnt 증가
                        home[a][b] = 0
                        Q.append((a,b))
            res.append(cnt)
    
print(len(res))
res.sort()
for m in res:
    print(m)


#DFS
# def DFS(x,y):
#     global cnt
#     cnt+=1 # 넘어온 좌표는 1을 만나서 온거
#     home[x][y]=0 #방문했으니 0으로 

#     for p in range(4):
#         a = x + dx[p]
#         b = y + dy[p]
#         if 0<=a<n and 0<=b<n and home[a][b]==1:
#             DFS(a,b)
    
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# n = int(input())
# res =[]
# home = [list(map(int,input())) for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if home[i][j] == 1: #1이면 집을 발견 거기서부터 퍼져나가야한다
#             cnt = 0 #집의 개수 카운팅, 매 단지가 발견될 때마다 cnt 0으로 초기화
#             DFS(i,j) #i,j좌표지점부터 퍼져나감
#             res.append(cnt) #res에 추가

# print(len(res))
# res.sort()
# for x in res:
#     print(x)

