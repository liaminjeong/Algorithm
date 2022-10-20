import sys
n = int(input())

N = map(int,sys.stdin.readline().split())
cnt = 0

for i in N:
    ch = [0]*i
    if i == 1:
        continue
    for j in range(2,i+1):
        if ch[j] == 0:
            cnt+=1
            for z in range(j,i+1,j):
                ch[z] =1
print(cnt)