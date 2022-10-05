import sys
from collections import deque

n,k = map(int,input().split())
no = list(range(1,n+1))
no = deque(no)
items = []

while len(no) >1 :
    for _ in range(k-1):
        cur = no.popleft()
        no.append(cur)

    items.append(no.popleft())

items.append(no[0])

print(f'<{", ".join(map(str,items))}>') #items를 str화하여 붙임
