import sys
def DFS(L,sum):
    if L == n and sum ==f: #종료지점 
        for x in p:
            print(x,end=' ')   # 만든수열 출력
        sys.exit(0) # 프로그램 완전 종료
    else:
        for i in range(1,n+1):
            if ch[i] ==0:
                ch[i] = 1
                p[L] = i
                DFS(L+1,sum+(p[L])*b[L]) # sum :p[L] *b[L]
                # p[0]번째에 1이 들어오면 그 1과 이항계수 리스트에 있는 0 번째 값을 
                # 곱한다 
                # 최종에 한번 곱하지 말고 한개한개 만들때마다 곱해서 위에서 sum 체크!!
                ch[i]=0

if __name__ == "__main__":
    n,f = map(int,input().split())
    p = [0]*n # 내가 만들 수열
    b = [1]*n # 이항계수  
    ch = [0]*(n+1) #체크리스트
    for i in range(1,n):
        # ex) n=4 이면 이항계수가 1 3 3 1 
        # 맨 앞과 맨 뒤는 1로 변하지 않기 때문에 0번째는 바꿔주지 않음
        b[i] = b[i-1]*(n-i) // i
        #  1     3      3       1
        # 3C0   3C1    3C2     3C3
        # 1/1   3/1   3*2/2*1   3*2*1/3*2*1
        # 분모는 b[i-1]번째 값에 (n-i)값을 곱해줌
        # 분자는 i 를 곱해줌 (i = 1,2,3)
        # 소수가 나와서 몫연산으로 변경
    DFS(0,0)