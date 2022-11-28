import sys
from collections import deque
# 시계방향으로 탐색하기 위한 dx,dy
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

# 체크리스트
ch = [[0]*n for _ in range(n)]

# 최종 답
sum = 0

Q = deque()

# 시작 값 체크리스트에 체크 
ch[n//2][n//2] =1

# 시작 값 sum에 더해줌
sum += a[n//2][n//2]

# Q에 튜플형태로 좌표 넣어줌 (시작점)
Q.append((n//2,n//2))

# 0 레벨부터 시작
L = 0

while True:
    if L == n//2: # 종료지점 -> 2
        break
    
    size = len(Q) # 현재 Q에 들어있는 값의 개수
    for i in range(size):
        tmp = Q.popleft() # 한개 pop되면 
        for j in range(4): # 4가지로 뻗음 
            # x,y좌표 바꾸면서 시계방향으로 탐색함
            x = tmp[0] + dx[j] #x좌표
            y = tmp[1] + dy[j] #y좌표
            
            if ch[x][y] == 0: # 좌표값이 탐색되지 않았으면
                sum += a[x][y]
                ch[x][y] = 1 # 탐색한 곳은 체크해줌
                Q.append((x,y))
    L +=1 # i가 끝나면 레벨탐색 끝난것 L 값 증가시켜줌
print(sum)
