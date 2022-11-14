import sys
def DFS(L,sum,time):
    global result
    if time  > m:
        return 
    if L == n:
        if result <sum:
            result = sum
    else:
        #문제 풀 경우 
        DFS(L+1,sum+pv[L],time+pt[L])

        #문제 안풀경우 (다음문제로..)
        DFS(L+1,sum,time)

n,m = map(int,input().split())
result = -2147000000
#n :문제의 개수
#m : 제한시간
pv = list() #문제점수
pt = list() #문제시간
for i in range(n):
    a,b = map(int,input().split())
    pv.append(a)
    pt.append(b)

DFS(0,0,0)
print(result)
