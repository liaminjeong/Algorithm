import sys
#그리디-정렬 세트
#회의가 끝나는시간을 기준으로 정렬한다
#시작시간이 빠른게 중요한게 아님 빨리끝나는게 중요함
n = int(input())
meeting = []
for i in range(n):
    s,e = map(int,input().split()) #s : 시작시간, e : 종료시간
    meeting.append((s,e)) #튜플형태로 리스트에 넣음

#정렬 (끝나는시간 기준)
meeting.sort(key=lambda x : (x[1],x[0]))
# x 가 meeting 리스트의 자료를 하나 받음
# return은 x[1]이 우선순위가 되고 x[0]이 차순이되라
# 끝나는 시간이 같으면 시작시간이 작은얘가 우선이 되겠지 

#원래 
#meeting.sort() = > 튜플이기 때문에 앞자료에 의해 정렬됨 
# 앞의 자료가 같으면 뒤의 자료값에 의해 정렬함

et = 0 #종료시간
cnt = 0 #개수

for s ,e in meeting: #s,e에 시작시간 종료시간 받아옴
    if s>=et: #시작시간이 종료시간보다 크면
        et = e #종료시간을 현재 받아온 종료시간으로 바꿔줌
        cnt+=1 #카운팅
print(cnt)


# input
# 5
# 1 4
# 2 3
# 3 5 
# 4 6
# 5 7