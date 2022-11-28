import sys
from collections import deque #큐사용

Max = 10000 #좌표의 max (직선의 좌표점은 1부터 1000)
ch = [0]*(Max+1) #체크리스트
dis = [0]*(Max+1)
n,m = map(int,input().split())

ch[n] = 1 
#처음 시작점 n
#n에서 시작하므로 ch(체크리스트)에 n번째에 1로 체크

dis[n] = 0
#그 거리 n번째에 자기자신이니까 0 넣는다

dQ = deque()
dQ.append(n) 
#큐에 출발점 추가 

while dQ: #위에서 dQ에 출발점 추가 했기때문에 dQ는 비어있지 않음
    now = dQ.popleft()
    if now == m: #종료지점
        break
    for next in (now-1,now+1,now+5):
        if 0<next<=max: #음수로는 갈 수 없고, max까지 니까
            if ch[next] ==0: # 방문 안했으면
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now]+1
print(dis[m])
