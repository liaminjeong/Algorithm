'''
풀어본 풀이
import sys
def check(x):
    for j in range(n):
        # if ch[y] != 1 and d[0]!=(x)+y and d[1]!= x-y: #(x+1+y)!=f and (y+1+y) !=s:
        if board[x] ==board[j] or 
            return False
        else:
            return False
    

def Nqueen(L):
    #print(L)
    global cnt
    print('L',L)
    if L ==n:
        cnt +=1 
        print('무야호호호호호호홓호호호호호호호호')
        return
    else:
        for i in range(n):
            board[L] = i
            if check(L):
                d[0] = L+i
                d[1] = L-i
                ch[i] =1
                Nqueen(L+1)
                ch[i] = 0
                d[0] = None
                d[1] = None
n = int(input())
ch= [0]*n
d=[None, None]
board = [None,None,None,None]
cnt = 0
Nqueen(0)
print(cnt)
'''


'''
블로그 풀이
def nqueen(depth):     
  global result
  
  # depth가 N일 때 > 모든 퀸을 다 놓은 것
  if depth == N : 
    result += 1 
    return 

  # depth별 반복문 
  for i in range(N):

    # 해당 depth를 visited 하지 않았을 때 
    #if visited[i] == False : 
    board[depth] = i     # (depth, i)에 퀸 올리기 (여기서 depth는 raw, i는 column에 해당
    
    if check(depth):
    #visited[i] = True
        nqueen(depth + 1)     # 그 다음 열로 넘어감 
    #visited[i] = False    # 다시 false로 설정해 백트래킹 


# 모든 열에대해 퀸과 대각선, 좌우에 위치해 있는지 체크 
def check(n):
  for i in range(n):

    # 좌우에 있거나, 대각선에 있다면 
    # TODO(여기서 기존 queen이 어떻게 적재되고 있는걸까?)
    #행의 거리와 열의 거리가 같은 곳에 있는 얘들은 대각선에 있음 
    #비교하는 행의 거리와 열의 거리가 같아서 abs절대값을 씌워주고 비교!
    if (board[n] == board[i]) or (n-i == abs(board[n] - board[i])):
      return False

  return True

# main 
if __name__ == '__main__':
  N = int(input())    # dfs의 depth에 해당함 
  # depth별 적재 
  board = [0] * N     # 1차원 리스트로 적재 
  visited = [False] * N
  result = 0 

  nqueen(0)
  print(result)
  '''


def dfs(L):
  global answer
  if L==n:
    answer += 1
    return

  for x in range(n):
    if x in col or (L-x) in diag1 or (L+x) in diag2:
      continue #아래 코드를 실행하지 않고 for문으로 올라가서 검사
    
    col.add(x)  #set에서 값 추가는 add
    diag1.add(L-x)  #오른쪽
    diag2.add(L+x)  #왼쪽
    dfs(L+1)
    col.remove(x) #set에서 값 삭제는 remove: 괄호의 값을 삭제
    diag1.remove(L-x)
    diag2.remove(L+x)

n = int(input())
#col,diag1,diag2검사할 set 
#set은 중복x 빈set은 set()으로 쓴다 
col, diag1, diag2 = set(), set(), set()
answer = 0
dfs(0)
print(answer)