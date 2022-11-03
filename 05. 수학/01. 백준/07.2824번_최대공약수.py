import sys
# 유클리드 호제로 A,B의 최대공약수 찾기
def getGdc(n,m):
    while m>0:
        n,m = m,n%m
    return n

n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))
A =1
B =1
for i in n_list:
    A *= i
for i in m_list:
    B *= i

print(str(getGdc(A,B))[-9:])





#22.10.27 내가 푼 풀이
# n = int(input())
# A = 1
# val = list(map(int, input().split()))
# for i in range(len(val)):
#     A*=val[i]

# m = int(input())
# B =1
# val2 = list(map(int,input().split()))
# for i in range(len(val2)):
#     B*= val2[i]

# #A를 소인수분해
# factor = 2
# factors = []
# while factor**2 <=A:
#     while A%factor ==0:
#         A=A//factor
#         factors.append(factor)
#     factor+=1

# if A>1:
#     factors.append(A)

# #B를 소인수분해
# factor2 = 2
# factors2 = []
# while factor2**2 <=B:
#     while B%factor2 ==0:
#         B=B//factor2
#         factors2.append(factor2)
#     factor2+=1

# if B>1:
#     factors2.append(B)

# i=0
# j=0
# common=[]
# gdc=1
# while i<len(factors) and j<len(factors2):
#     if factors[i] == factors2[j]:
#         common.append(factors[i])
#         i+=1
#         j+=1
#     elif factors[i] < factors2[j]:
#         i+=1
#     else:
#         j+=1
# for i in common:
#     gdc *=i

# if len(str(gdc)) >9:
#     gdc = str(gdc)[-9:]
# print(gdc)