import sys
from collections import deque
f,s,g,u,d = map(int,input().split())
dis = [0]*(f+1)
ch = [0]*(f+1)
Q = deque()
Q.append(s)
dis[s] = 0
ch[s] = 1
while Q:
    now = Q.popleft()
    if now == g:
        print(dis[now])
    for next in (now+u,now-d):
        if 0<next<=f and ch[next]==0:
            Q.append(next)
            ch[next] = 1
            dis[next] = dis[now]+1

if ch[g] ==0:
    print('use the stairs')



# if s==g or s<1 or u<0 or d>1000000 or 1000000<f<g:
#     print('use the stairs')
#     sys.exit()
# if s>g and d==0:
#     print('use the stairs')
#     sys.exit()

