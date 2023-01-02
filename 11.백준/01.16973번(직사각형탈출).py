import sys
sys.setrecursionlimit(10**6)
from collections import deque

#왼,오,위,아래 탐색위한 좌표
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
ch = [[0]*(m+1) for _ in range(n+1)] #체크배열
# 2차원 배열의 누적합
#psum 테이블은 기존 board보다 하나씩 크게 하는게 편하다
psum = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        psum[i][j] = psum[i-1][j]+psum[i][j-1]-psum[i-1][j-1]+board[i-1][j-1]
        #board의 위쪽 왼쪽값을 더해주고 대각선의 값을 빼준다음 board 자기자신의 값 더해준다

h,w,sr,sc,fr,fc = map(int,input().split())
sr,sc,fr,fc = sr-1,sc-1,fr-1,fc-1

Q = deque()
Q.append((sr,sc))
ch[sr][sc] = 1

cnt = 0
while Q:
    tmp = Q.popleft()
    if tmp[0]== fr and tmp[1]==fc:
        break

    for i in range(4):
        a = tmp[0] + dx[i]
        b = tmp[1] + dy[i]
        x1,y1 = a+1,b+1 #psum은 0부터 시작하고 board는 1부터 시작하기 때문에 a,b에 +1한다
        x2,y2 = x1+h-1,y1+w-1 #사각형의 범위
        if 0<=a<=n and 0<=b<=m and a+h<=n and b+w<=m and not(psum[x2][y2]-psum[x2][y1-1]-psum[x1-1][y2]+psum[x1-1][y1-1] >0) :
            if ch[a][b]==0 and board[a][b]==0:
                cnt+=1
                Q.append((a,b))
                ch[a][b]=ch[tmp[0]][tmp[1]]+1 
print(ch[fr][fc]-1)




#2차원 배열의 누적합
#2차원 배열 arr이 있을 때, arr[x1][y1]부터 arr[x2][y2]까지의 부분 배열의 
# 합을 Range(x1, y1, x2, y2)라 하자. 
# 그리고 누적합 배열 S로 다음과 같이 정의된다.
#Range(x1, y1, x2, y2) = S(x2, y2) - S(x1, y2) - S(x2, y1) + S(x1, y1)






# input
# 4 5
# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 2 2 1 1 1 4



