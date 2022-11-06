import sys
import itertools as it #itertools -> 순열, 조합 자동으로 구해줌

n,f = map(int,input().split())
b = [1]*n
for i in range(1,n):
    b[i] = b[i-1]*(n-1)/i
a = list(range(1,n+1))
cnt = 0

for tmp in it.permutations(a):
    #permutations(a) -> a에 있는자료를 모든 순열로 구해줌
    #하나의 순열이 구해지면 tmp에 튜플로 저장됨
    #permutations(a,3) - > a리스트에서 3개만 뽑아라
    sum = 0
    for L,x in enumerate(tmp):
        sum += [x*b[L]]
        #sum 이 다 더해짐

    if sum == f:
        for x in tmp:
            print(x,end=' ')
        break #이 break는 제일위의 for문 break한다