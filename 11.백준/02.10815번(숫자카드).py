import sys
def Stat(num):
    for i in ch:
        if ch[i] == card[num]:
            return True
        else:
            return False
n = int(input())
card = list(map(int,input().split()))
m = int(input())
ch  = list(map(int,input().split()))
card.sort()
lt = 0
rt = n-1
while lt <=rt:
    mid = (lt+rt)//2 #2
    if Stat(mid):
        print(1,end=' ')

    else:
        print(0,end=' ')