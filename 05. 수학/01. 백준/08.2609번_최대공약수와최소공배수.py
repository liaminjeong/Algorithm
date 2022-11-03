import sys
n,m = list(map(int,sys.stdin.readline().split()))

#최대공약수
#유클리드호제
def getGdc(n,m):
    while m>0:
        n,m = m,n%m
    return  n
print(getGdc(n,m))
#최소공배수
lcm = n*m//getGdc(n,m)
print(lcm)






#내가 푼것
#n의 소인수 분해 
# factor =2
# factors = []
# while factor**2 <=n:
#     while n%factor == 0:
#         n = n//factor
#         factors.append(factor)
#     factor+=1
# if n>1:
#     factors.append(n)

# #m의 소인수분해
# factor2 = 2
# factors2 =[]
# while factor2 **2<=m:
#     while m%factor2 == 0:
#         m = m//factor2
#         factors2.append(factor2)
#     factor2+=1
# if m>1:
#     factors2.append(m)

# #최소공배수
# i=0
# j=0
# res =[]
# while i<len(factors) and j<len(factors2):
#     if factors[i] == factors2[j]:
#         res.append(factors[i])
#         i+=1
#         j+=1
#     elif factors[i] <factors2[j]:
#         res.append(factors[i])
#         i+=1
#     else:
#         res.append(factors2[j])
#         j+=1

# while i<len(factors):
#     res.append(factor[i])
#     i+=1
# while j <len(factors2):
#     res.append(factors2[j])
#     j+=1

# lcm =1
# for x in res:
#     lcm*=x
# print(lcm)


