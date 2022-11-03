import sys
def DFS(v):
    if v>7:
        return
    else:
        #전위
        print(v)
        DFS(v*2)
        DFS(v*2+1)

        #중위
        DFS(v*2)
        print(v)
        DFS(v*2+1)

        #후위
        DFS(v*2)
        DFS(v*2+1)
        print(v)

if __name__ == "__main__":
    DFS(n)
