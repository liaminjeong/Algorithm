import sys
sys.setrecursionlimit(10**6)
def DFS(x,y):
    ch[x][y] = 1
    if x==0:
        print(y)
    else:
        #왼쪽
        if 0<=y-1 and sadari[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x,y-1)
        #오른쪽
        elif y+1<10 and sadari[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x,y+1)
        else:
            DFS(x-1,y)

sadari = [list(map(int,sys.stdin.readline().split())) for _ in range(10)]
ch = [[0]*10 for _ in range(10)]
for y in range(10):
    if sadari[9][y] ==2:
        DFS(9,y)
