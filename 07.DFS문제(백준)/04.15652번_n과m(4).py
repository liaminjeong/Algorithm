import sys
def DFS(L,s):
    if L == m:
        for j in range(len(res)):
            print(res[j],end=' ')
        print()
    else:
        for i in range(s,n+1):
            res[L]=i
            DFS(L+1,i)  #다음시작점 i 왜? 중복이니까!!

if __name__== "__main__":
    n,m = map(int,input().split())
    res = [0]*m
    DFS(0,1)

#중복조합