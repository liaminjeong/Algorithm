import sys
def DFS(v):
    if v == m:
        for j in range(v):
            print(res[j],end= ' ')
        print()  
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i] =1
                res[v] = i
                DFS(v+1)
                ch[i] = 0

if __name__ == "__main__":
    n,m = map(int,input().split())
    ch = [0]*(n+1)
    res = [0]*(m+1)
    DFS(0)