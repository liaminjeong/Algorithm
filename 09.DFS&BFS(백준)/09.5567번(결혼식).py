# import sys
# from collections import deque
# n = int(input())
# m = int(input())
# list = [[0]*(n+1) for _ in range(n+1)]
# ch = [0]*(n+1)
# cnt = 0
# Q = deque()
# for i in range(m):
#     a,b = map(int,input().split())
#     list[a][b] = 1

# Q.append(1)
# ch[1] = 1
# while Q:
#     now = Q.popleft()
# for i in range(n+1):
#     for j in range(n+1):
#         for p in range(4):
#             a = i+dx[p]
#             b = j+dy[p]
#             if 0<=a<n and 0<=b<n and dongList[a][b]==1:
#                 cnt+=1


