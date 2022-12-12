import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def DFS(v):
    ch[v] = 1
    for  i in range(1,n+1):
        if g[v][i] ==1 and ch[i]==0:
            DFS(i)

n,m = map(int,input().split())
g = [[0]*(n+1) for _ in range(n+1)]
ch = [0]*(n+1)
cnt = 0
for i in range(m):
    a,b = map(int,input().split())
    g[a][b] = 1
    g[b][a] = 1

for i in range(1,n+1):
    if ch[i] ==0:
        DFS(i)
        cnt+=1
print(cnt)







# Q = deque()
# Q.append(1)
# ch[1] = 1
# while Q:
#     tmp = Q.popleft()
#     print('tmp: ',tmp)
#     for i in range(1,n+1):
#         if g[tmp][i] ==1 and ch[i]==0:
#             ch[i] = 1
#             Q.append(i)
# cnt+=1
# print(cnt)
