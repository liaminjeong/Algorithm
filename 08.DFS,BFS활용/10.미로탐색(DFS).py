# import sys
# def DFS(x,y):
#     if board[6][6] ==1:
#         cnt+=1
#     else:
#         for i in range(7):
#             for j in range(7):
#                 print('i: ',i,'j: ',j,end=' ')
#                 print()
#                 if board[i][j] ==0:#ch[i][j]==0 and :
#                     for p in range(4):
#                         a = i + dx[p]
#                         b = j + dy[p]
#                         print('a: ',a,'b: ',b,end=' ')
#                         print()
#                         if 0<=a<7 and 0<=b<7:
#                             print('여기!!!!!!!!!!!')
#                             #ch[a][b] = 1
#                             board[a][b]=1
#                             DFS(a,b)
#                             #ch[a][b] = 0
#                             board[a][b]=0

        
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# board = [list(map(int,input().split())) for _ in range(7)]
# #ch = [[0]*7 for _ in range(7)]

# cnt = 0
# DFS(0,0)
# print(cnt)


import sys
def DFS(x,y):
    global cnt
    if x == 6 and y ==6:
        cnt+=1
    else:
        # if board[x][y] == 0:
        #     board[x][y] = 1
        for p in range(4):
            a = x + dx[p]
            b = y + dy[p]
            if 0<=a<7 and 0<=b<7 and board[a][b]==0:
                board[a][b]=1
                DFS(a,b)
                board[a][b]=0

        
dx = [-1,0,1,0]
dy = [0,1,0,-1]
board = [list(map(int,input().split())) for _ in range(7)]
board[0][0]=1 #board에 체크해줌
cnt = 0
DFS(0,0)
print(cnt)

