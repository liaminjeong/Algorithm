import sys
from collections import deque

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    pil = sys.stdin.readline().split()
    
    Q2 = deque([(pos,val) for pos,val in enumerate(map(int,list(pil)))])
    cnt = 0

    while True:
        cur = Q2.popleft() #하나를 pop()
        if any(cur[1]<x[1] for x in Q2):
            #이미 하나 popleft 했으니까 Q2는 2번째꺼부터비교
            #하나씩비교x 하나뽑은거와 나머지 통으로 비교
            Q2.append(cur)
        else:
            cnt +=1 #순번
            if cur[0]== m:
                break
    print(cnt)

# 궁금증@
#any라는 함수로 
