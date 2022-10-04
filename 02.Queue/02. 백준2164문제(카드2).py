import sys
from collections import deque

n =  int(input())
items = list(range(1,n+1))
items = deque(items) #items를 큐화함

while len(items) > 1: #조건이 참인동안에 while문 돈다 조건 거짓이면 나감
    items.popleft()
    items.append(items.popleft())
print(items[0])
