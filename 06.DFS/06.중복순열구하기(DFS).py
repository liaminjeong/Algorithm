import sys
def DFS(L):
    global cnt
    if L == m: #종료지점
        for j in range(m):
            print(res[j],end=' ')
        print() #줄바꿈
        cnt +=1
    else:
        for i in range(1,n+1): #뻗어지는 가지 수 즉, 뽑을 수 있는 구슬
            res[L] = i
            # 다음 함수 호출하기 전에 무조건 실행한다
            DFS(L+1)

if __name__ == "__main__":
    n,m = map(int,input().split()) #m:뽑는 횟수
    res = [0]*m
    cnt = 0 
    DFS(0)
    print(cnt)