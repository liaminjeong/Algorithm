import sys
n = int(input()) #지원자의 수 
body = []
for i in range(n):
    h,w = map(int,input().split())
    body.append((h,w))
body.sort(reverse=True) #키순으로 정렬(내림차순 정렬)
# 키 순으로 정렬하면 맨 위의 사람은 다른사람보다 키가 크니까 카운팅
# 다음사람은 내 아래는 다 키가 작으니까 나보다 키가 큰사람들 중에서 내가 
# 몸무게가 가장 많아야함 
# 이런식으로 위의 사람과 비교함

cnt = 0 # 뽑히는 인원 수 
max = 0 # 최대값(몸무게)
for h,w in body: #h:키,w:몸무게
    if w>max: #몸무게가 max보다 크면
        max = w #최대값을 갱신함
        cnt+=1 #최대값 갱신될때만 카운팅
print(cnt)

#input
# 5
# 172 67
# 183 65
# 180 70
# 170 72
# 181 60