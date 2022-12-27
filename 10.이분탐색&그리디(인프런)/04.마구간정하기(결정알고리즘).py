import sys
def Count(len):
    cnt = 1 #말 한마리를 배치한다
    #어디다가?
    ep = horse[0] # 말이 마지막에 배치된 지점

    for i in range(1,n-1): #위에서 첫번째 마구간 했으니까 1번부터 시작
        # horse[i]지점은 두번 째 말을 배치하려는 곳
        if horse[i]-ep>=len:
        # 현재 놓아보려는 지점 - 마지막에 놓은지점 = 거리
            cnt+=1
            ep = horse[i] #마지막 말 놓은곳으로 바꿔줌
    return cnt
n,c = map(int,input().split())
horse=[]
for i in range(n):
    a = int(input())
    horse.append(a)
horse.sort() #마구간 좌표 정렬

lt,rt = 1,horse[n-1]
while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid)>=c: # mid : 가장가까운 두 말의 거리
        # Count 함수 : 배치할 수 있는 말의 마리수를 return
        # 그게 c보다 크거나 같으면 mid 가 답이 될 수 있다 
        res = mid # 답
        # 가장 인접한 두 말의 최대 
        lt = mid+1
    else: #거리가 너무 길어서 원하는 마리수를 다 배치하지 못하는 상태
        # 더 좁혀야함 큰 값은 날려야 함
        rt = mid -1

print(res)
