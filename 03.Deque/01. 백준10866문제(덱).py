import sys
from collections import deque

n = int(input())
items = list()
items = deque(items)

for _ in range(n):
    val = sys.stdin.readline().split()
    if val[0] == 'push_front':
        items.appendleft(val[1])
    if val[0] == 'push_back':
        items.append(val[1])
    if val[0] == 'pop_front':
        if len(items) == 0:
            print('-1')
        else:
            print(items.popleft())
    if val[0] == 'pop_back':
        if len(items) == 0:
            print('-1')
        else:
            print(items.pop())
    if val[0] == 'size':
        print(len(items))
    if val[0] == 'empty':
        if len(items) == 0:
            print('1')
        else:
            print('0')
    if val[0] == 'front':
        if len(items) == 0:
            print('-1')
        else:
            print(items[0])
    if val[0] == 'back':
        if len(items) == 0:
            print('-1')
        else:
            print(items[-1])
