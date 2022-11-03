import sys

m,n = map(int,input().split()) 

for i in range(m,n+1):
    if i ==1:
        continue
    for j in range(2,int(i** 0.5)+1):
        if i%j ==0:
            break
    else:
        print(i)

ch = [0]*(n+1)
res = []
for i in range(2,n+1):
    if i==1:
        continue
    if ch[i] == 0:
        res.append(i)
    for j in range(i*2,n+1,i):
        ch[j] =1

for i in res:
    if i < m:
        res.remove(i)
print(res)



    

