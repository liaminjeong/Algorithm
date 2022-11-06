import sys
n,m = map(int,input().split())
#n : 노드개수
#m : 간선의 개수
g = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):

# 무방향그래프
# 방향이 없다
    a,b = map(int,input().split())
    g[a][b] = 1
    g[b][a] = 1
    #기본이 0으로 초기화 되어있다고 생각하며
    #가면 1로 바꿔줌
    #무방향이기 때문에 a행에서 b열로 b행에서 a열로 가는것 
    #둘다 1로 체크해줌

# 방향그래프
    a,b,c = map(int,input().split())
    g[a][b] = c #a->b 를 c가중치로 바꿔줌

# 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        print(g[i][j],end=' ')
    print()
