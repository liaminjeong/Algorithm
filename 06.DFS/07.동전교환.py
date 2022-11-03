import sys

def DFS(L,sum):
    global res
    if L>res:# L(레벨)이 res(현재구한 동전개수)보다 크면 나머지는 판단할 필요 없음
        return
    if sum > m:
        return 
    if sum == m:
        if L<res:
            res = L
        print(res)
    else:
        for i in range(n):
            DFS(L+1,sum+a[i])

if __name__ == "__main__":
    n = int(input()) #동전의 종류 개수 
    a = list(map(int,input().split())) #동전의 종류 즉, 뻗어나갈 가지
    m = int(input())
    res = 2147000000
    a.sort(reverse = True) #큰 값 부터 판단하기 위해서 
    DFS(0,0)
    print(res)