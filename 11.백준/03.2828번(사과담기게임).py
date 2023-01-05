import sys
n ,m = map(int,input().split())
j = int(input()) #사과개수

l = 1 #바구니의 왼쪽좌표
r = m #바구니의 오른쪽 좌표
sum = 0 #이동거리
for i in range(j):
    position = int(input()) #사과의 위치

    if l<=position and position<=r: #사과의위치가 바구니의 위치 안에 있을경우
        #즉, 사과가 바구니에 떨어지면
        continue
    elif l>position:#사과가 바구니 왼쪽가깝게 떨어지면
        sum += (l-position)
        r -=(l-position)
        l = position
    else: #바구니의 오른쪽에 가깝게 떨어지면
        sum +=(position-r)
        l +=(position-r)
        r =  position
print(sum)

