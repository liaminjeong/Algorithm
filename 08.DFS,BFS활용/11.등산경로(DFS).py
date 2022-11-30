import sys
def DFS(x,y):
    global cnt
    if x==ex and y ==ey:
        cnt+=1
    else:
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<n and 0<=b<n and ch[a][b]==0 and gil[x][y] < gil[a][b]:
                ch[a][b] = 1
                DFS(a,b)
                ch[a][b]=0


dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(input())
gil = [list(map(int,input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
min = 2147000000
max = -2147000000
#가장 낮은지점과 높은지점의 좌표
for i in range(n):
    for j in range(n):
        if gil[i][j] < min:
            min = gil[i][j]
            sx = i
            sy = j
        if gil[i][j] > max:
            max = gil[i][j]
            ex= i
            ey= j

ch[sx][sy] = 1         
cnt=0
DFS(sx,sy)
print(cnt)
#현재지점보다 앞으로 갈 수 있는 값이 커야 갈 수 있다

#인프런은 처음에 input안받음
# gil = [[0]*n for _ in range(n)]
# for i in range(n):
#     tmp = list(map(int,input().split())) # input한줄 받음
#     for j in range(n):
#         if tmp[j] < min:
#             min = tmp[j]
#             sx = i
#             sy = j
#         if tmp[j]>max:
#             max = tmp[j]
#             ex = i
#             ey = i
#         gil[i][j] = tmp[j]