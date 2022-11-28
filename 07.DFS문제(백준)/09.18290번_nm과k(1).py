import sys
def DFS(L,x,y,sum):
    global res
    if L == k:
        if res<sum:
            res = sum
    else:
        for i in range(x,n):
            for j in range(y if i==x else 0,m):
               
                if ch[i][j] == 0:           
                    for z in range(4):
                        a = i + dx[z]
                        b = j + dy[z]

                        if 0<=a<n and 0<=b<m:
                            if ch[a][b] == 1:  
                                break             
                    else:
                        ch[i][j] = 1
                        DFS(L+1,i,j,sum+g[i][j])
                        ch[i][j] = 0

                        
dx = [-1,0,1,0]
dy = [0,1,0,-1]
n,m,k = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(n)]
ch = [[0]*m for _ in range(n)]
res = -10000

DFS(0,0,0,0)
print(res)















# def DFS(L,x,y,sum):
#     global res
#     if L == k:
#         if res<sum:
#             res = sum
#     else:
#         print('x : ',x,'y: ',y,end=' ')
#         print()
#         for i in range(x,n):
#             for j in range(y if i==x else 0,m):
#                 print('i: ',i,'j: ',j,end=' ')
#                 print()
#                 if ch[i][j] == 0:
#                     ch[i][j] = 1
#                     for z in range(4):
#                         a = x + dx[z]
#                         b = y + dy[z]
#                         print('a: ',a,'b: ', b,end=' ')
#                         print()
                        
#                         if 0<=a<=4 and 0<=b<=4:
#                             ch[a][b] = 1
#                             print(ch)
#                     DFS(L+1,i,j,sum+g[i][j])
#                     ch[i][j] = 0

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# n,m,k = map(int,input().split())
# g = [list(map(int,input().split())) for _ in range(n)]
# ch = [[0]*n for _ in range(n)]
# res = -10000

# DFS(0,0,0,0)
# print(res)




# for i in range(n):
#             for j in range(m):
#                 print('i : ',i,'j : ',j,end='')
#                 print()
#                 if ch[i][j] ==0:
#                     ch[i][j] = 1
#                     for p in range(4):
#                         a = x+dx[p]
#                         b = y+dy[p]
#                         if 0<=a<=4 and 0<=b<=4:
#                             ch[a][b] = 1
#                             DFS(L+1,x+i,y+j,sum+g[i][j])
#                             ch[a][b] = 0
#                             ch[x][y]=0 
        

