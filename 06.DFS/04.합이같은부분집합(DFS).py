import sys
def DFS(L,sum):
    if sum > total//2: #내가 만든 합(sum)이 전체합(total)의 반보다 크면
        return
    
    if L == n: #종료지점
        if sum == (total-sum): #total-sum ->선택안된원소의 합
            print("YES")
            sys.exit(0) #프로그램 종료
        else:
            #사용할 경우
            DFS(L+1, sum+a[L]) #idx 1씩 증가하고 sum은 리스트의 L번째 사용
            #사용하지 않을 경우
            DFS(L+1,sum) #그 전단계의 sum


if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    total = sum(a) #전체total은 리스트a의 합
    DFS(0,0) #idx,sum
    print("NO")