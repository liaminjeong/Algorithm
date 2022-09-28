'''
괄호
'''

import sys

T = int(input())

for _ in range(T):
    items = []
    val = sys.stdin.readline().strip()
    for j in val:
        if j == '(':
            items.append(j)
        elif j == ')':
            if len(items) == 0:
                print('NO')
                break
            else:
                items.pop()
    else:
        if len(items) == 0:
            print('YES')
        else:
            print('NO')
