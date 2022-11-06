import sys
def DFS(v):
    global cnt
    if v == n:
        cnt+=1
        #for x in path:
            #print(x,end = ' ')
        #print()
    else:
        for i in range(1,n+1):
            if g[v][i] == 1 and ch[i]==0:
                #v번노드에서 i번 노드로 연결되있는지
                #ch[i]번째로 갈 수 있는지
                ch[i] =1
                #path.append(i)
                DFS(i)
                #path.pop()
                ch[i]=0

if __name__ == "__main__":
    n,m = map(int,input().split())
    g = [[0]*(n+1) for _ in range(n+1)]
    ch = [0]*(n+1) # 체크리스트
    for i in range(m):
        a,b = map(int,input().split())
        g[a][b]=1
    cnt = 0
    #path = []
    #path.append(1)
    ch[1] = 1 #1번노드 방문했다 체크
    DFS(1)