import sys
sys.setrecursionlimit(10**6)
# # DFS
# def DFS(x,y):
#     global cnt
#     land[x][y] = 0
#     for p in range(8):
#         a = x + dx[p]
#         b = y + dy[p]
#         if 0<=a<h and 0<=b<w and land[a][b]==1:
#             land[a][b] = 0
#             DFS(a,b)
    
        
# dx = [-1,-1,0,1,1,1,0,-1]
# dy = [0,1,1,1,0,-1,-1,-1,0]

# while True:
#     w,h = map(int,input().split())
#     if w ==0 and h==0:
#         break
#     land = [list(map(int,input().split())) for _ in range(h)]
#     cnt = 0
#     for i in range(h):
#         for j in range(w):
#             if land[i][j] ==1:
#                 cnt+=1
#                 DFS(i,j)
#     print(cnt)




                
