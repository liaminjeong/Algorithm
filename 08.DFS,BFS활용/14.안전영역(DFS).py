import sys
sys.setrecursionlimit(10**6) #파이썬에서 재귀함수 할때 백준사이트에서 런타임에러 날때

# >>> 백준에서 DFS,BFS둘다 테스트 해보기

# <<<DFS>>> me
# def DFS(h,x,y): #높이,시작,끝점
#     print('h: ',h,'x: ',x,'y: ',y,end=' ')
#     print()
#     ch[x][y] = 1
#     for p in range(4):
#         a = x + dx[p]
#         b = y + dy[p]
#         if 0<=a<n and 0<=b<n and region[a][b] >h:
#             ch[a][b] = 1
#             DFS(h,a,b)
#     cnt+=1
#     res.append(cnt)


# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# n = int(input())
# region = [list(map(int,input().split())) for _ in range(n)]
# max = max(map(max,region)) #이차원리스트의 최대값구해줌
# res = []
# for r in range(max):
#     cnt = 0
#     ch = [[0]*n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if region[i][j] > r:
#                 sx = i
#                 sy = j
#                 DFS(,sx,sy)

# print(max(res))

#<<<DFS>>> 인프런
# def DFS(H,x,y):
#     ch[x][y] =1
#     for p in range(4):
#         a = x + dx[p]
#         b = y + dy[p]
#         if 0<=a<n and 0<=b<n and ch[a][b]==0 and region[a][b]>H:
#             DFS(H,a,b)

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# n = int(input())
# region = [list(map(int,input().split())) for _ in range(n)]
# cnt = 0 #높이 정하고 안전영역이 뭐인가
# res = 0 #최종적인 답
# for h in range(100): #0~99까지
#     ch = [[0]*n for _ in range(n)] #높이가 바뀔때마다 0으로 초기화
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if ch[i][j] ==0 and region[i][j]>h:
#                 cnt+=1
#                 DFS(h,i,j)
#     res = max(res,cnt)
#     if cnt == 0 : #9가 됐을때
#         break
# print(res)

#<<<BFS>>>
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(input())
region = [list(map(int,input().split())) for _ in range(n)]
Q = deque()
cnt = 0
res = 0
for h in range(100):
    ch = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if ch[i][j] == 0 and region[i][j] > h:
                sx = i
                sy = j
                ch[i][j] =1
                cnt +=1
                Q.append((i,j))

                while Q:
                    tmp = Q.popleft()
                    for p in range(4):
                        a = tmp[0] + dx[p]
                        b = tmp[1] + dy[p]
                        if 0<=a<n and 0<=b<n and ch[a][b]==0 and region[a][b]>h:
                            ch[a][b] = 1
                            Q.append((a,b))
    if cnt == 0:
        break
    res = max(res,cnt)
print(res)
