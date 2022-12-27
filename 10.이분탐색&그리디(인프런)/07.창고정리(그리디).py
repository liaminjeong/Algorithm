import sys
l = int(input()) #창고의 가로길이
h = list(map(int,input().split()))
m = int(input())
h.sort() #sort 하면 가장 작은 값과 가장 큰 값이 정렬이 됨
for _ in range(m):
    h[0]+=1 #h[0]는 가장작은값이 될거고 거기에 +1해줌
    h[l-1]-=1 #h[l-1]은 가장 큰 값이 될거고 거기에 -1해줌
    h.sort() # 매번 sort해줌
print(h[l-1]-h[0])