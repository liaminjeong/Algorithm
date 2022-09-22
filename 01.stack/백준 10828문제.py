import sys

N =  int(input())

items = []

for i in range(N):
    val = sys.stdin.readline().split()  #strip
    if val[0] == 'push':
        items.append(val[1])
    elif val[0] == 'pop':
        if len(items) == 0:
            print(-1)
        else:
             print(items[-1])
             items.pop()
    elif val[0] == 'size':
        print(len(items))
    elif val[0] == 'empty':
        if len(items) == 0:
            print(1)
        else:
            print(0)
    elif val[0] == 'top':
        if len(items) > 0:
            print(items[-1])
        else:
            print(-1)

    
