import sys
def DFS(L,sum):
    global res
    if L == n+1: #종료지점
        if res<sum:
            res = sum
    else:
        #상담을 하는 경우
        if L+T[L] <=n+1:
            # 만약 넘어온 날짜와 그 상담이 걸리는날짜의 합이 n+1보다 작아야 가지 뻗음
            # L+T[L] --> 다음상담날짜가 됨
            DFS(L+T[L],sum+P[L]) # 다음상담일자로 이동함
        #상담안하는 경우
        DFS(L+1,sum)
        # 그냥 다음날짜로 넘어감
        
            
if __name__ == "__main__":
    n = int(input())
    T = list() #걸린시간
    P = list() #얻을 수 있는 금액
    for i in range(n):
        a,b = map(int,input().split())
        T.append(a)
        P.append(b)
    res = -2147000000
    T.insert(0,0) #T리스트에 인덱스를 날짜로 인식하려고
    P.insert(0,0)
    # T,P리스트 모두 for 문돌면서 0번인덱스부터 시작함
    # 그 인덱스를 문제의 표에 나온것 처럼 날짜로 두려고 맨앞에 0을 insert함
    DFS(1,0)
    # 1 :날짜 0 : 수익총합







# 먼저푼풀이
# def DFS(L,t,p):
#     global res
#     if t>n:
#         return
#     if L == n+1:
#         if res < p:
#             res = p
#     else:
#         DFS(L+pt[L],t+pt[L],p+pp[L])
#         DFS(L+pt[L],t,p)
# n = int(input())
# res = -2147000000
# pt = list()
# pp = list()
# for i in range(n):
#     a,b = map(int,input().split())
#     pt.append(a)
#     pp.append(b)

# DFS(0,0,0)
# print(res)
