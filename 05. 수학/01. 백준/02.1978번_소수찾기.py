import sys
n = int(input())

N = list(map(int,sys.stdin.readline().split()))
print(N)
cnt = 0

# for i in n:
#     ch = [0]*(i+1)
#     for j in range(2,n+1):  
#         if ch[j] ==0:
#             cnt+=1
#         for x in ragne(j+1, n+1)
# print(cnt)

for _ in range(n):
    for i in N:
        if i ==1:
            continue
        ch = [0]*(i+1)
        for j in range(2,i+1):
            if ch[j] == 0:
                cnt+=1
            for x in range(j+1,i+1,j):
                ch[x] =1
    print(cnt)
