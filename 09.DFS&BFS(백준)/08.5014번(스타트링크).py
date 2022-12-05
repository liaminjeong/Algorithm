import sys
from collections import deque
f,s,g,u,d = map(int(input().split()))
dis = [0]*(f+1)
Q = deque()
Q.append(s)
dis[s] = 0
# while Q:
#     tmp = Q.popleft()
#     if

