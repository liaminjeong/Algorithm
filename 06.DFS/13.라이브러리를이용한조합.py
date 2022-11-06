import sys
import itertools as it

n,k = map(int,input().split())
a = list(map(int,input().split()))
m = int(input())
cnt = 0

for x in it.combinations(a,k):
    #combinations(a,k) -> 조합구해줌 a리스트 중 k개
    if sum(x)%m ==0:
        #x는 만들어진 조합의 리스트
        #따라서 sum(x)는 만들어진 하나의 리스트이다
        cnt+=1
print(cnt)
    