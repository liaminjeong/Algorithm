import sys
#L:idx, sum:만든 부분집합 합, tsum:판단(o냐x냐) 바둑이의 무게합
def DFS(L,sum,tsum): 
    global result
    if sum +(total-tsum) <result:
        return 
    #내가 만든 부분집합의 합(sum)과 
    #전체무게에서 부분집합에 넣던 넣지 않던 판단을 한 값을 뺀값 
    #즉, 앞으로 판단해야 할 값들의 합을 더한게 
    #내가 가지고있는 최적의 값 result보다 작으면 더 볼 필요 x

    if sum > c:
        return 
    #내가 만든 부분집합의 합(sum)이 무게제한(c)보다 크면 return 

    if L == n: #종료지점
        if sum > result:
            result = sum
        #내가 만든 부분집합의 합이 현재 가지고 있는 최적의 합보다 크면
        #최적의 합result를 sum값으로 바꿈
    else:
        DFS(L+1,sum+a[L],tsum+a[L]) # 바둑이 태운다
        DFS(L+1,sum,tsum+a[L])      # 바둑이 태우지 않는다
        #여기서 tsum+a[L] : 판단을 한 무게의 합


if __name__ == "__main__":
    c,n = map(int,input().split()) #c:무게제한, n:바둑이수
    a = [0]*n #a리스트 초기화 
    result = -2147000000 #제일 작은 값으로 초기화 
    for i in range(n):
        a[i]  = int(input()) #각각의 바둑이 무게를 a에 넣어줌
    total = sum(a) #총 바둑이의 무게 
    DFS(0,0,0)
    print(result)
    

