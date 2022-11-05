import sys
def DFS(L,s,sum):
    global cnt
    if L ==k:
        if sum%m ==0:
            cnt+=1
    else:
        for i in range(s,n): #n-1번째까지 돌아야 함
            #리스트 a에는 0부터 n-1번째 까지 들어가 있으므로!!
            DFS(L+1,i+1,sum+a[i])

if __name__=="__main__":
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    m = int(input())
    cnt = 0
    DFS(0,0,0)
    print(cnt)