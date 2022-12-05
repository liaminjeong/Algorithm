import sys
sys.setrecursionlimit(10**6)
#DFS
def DFS(x,y):
    global cnt
    cabbage[x][y]=0
    for p in range(4):
        a = x+dx[p]
        b = y+dy[p]
        if 0<=a<n and 0<=b<m and cabbage[a][b] ==1:
            DFS(a,b)

dx = [-1,0,1,0]
dy = [0,1,0,-1]
t = int(input())

for _ in range(t):
    m,n,k = map(int,input().split())
    cabbage = [[0]*m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x,y = map(int,input().split())
        cabbage[y][x] = 1

    for i in range(n):
        for j in range(m):
            if cabbage[i][j]==1:
                cnt+=1
                DFS(i,j)

    print(cnt) #답출력
    