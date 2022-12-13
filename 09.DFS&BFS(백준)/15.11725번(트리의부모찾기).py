# import sys
# sys.setrecursionlimit(10**6)
# def DFS(v):
#     ch[v] =1
#     for i in range(1,n+1):
#         if g[v][i]==1 and ch[i]==0:
#             parent[i] = v
#             DFS(i)
# n = int(input())
# g = [[0]*(n+1) for _ in range(n+1)]
# ch = [0]*(n+1)
# parent = [0]*(n+1)
# for i in range(n-1):
#     a,b = map(int,input().split())
#     g[a][b] = 1
#     g[b][a] = 1

# DFS(1)

# for x in range(2,n+1):
#     print(parent[x])


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def DFS(v):
    ch[v] =1
    for i in range(1,n+1):
        if i in g[v] and ch[i]==0:
            parent[i] = v
            DFS(i)
n = int(input())
g = [[] for _ in range(n+1)]
ch = [0]*(n+1)
parent = [0]*(n+1)
for i in range(n-1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

DFS(1)

for x in range(2,n+1):
    print(parent[x])




