import sys
def Count(len): #n개의 랜선의 길이 매개변수, 개수를 return
    cnt = 0
    for x in Line:
        cnt+=(x//len) #만들어낼 수 있는 작은 토막의 개수
    return cnt

k,n = map(int,input().split())
Line = []
res = 0
largest = 0 # 가장 긴 랜선
for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    #범위 1~ 가장긴 랜선의 길이까지!!
    largest = max(largest,tmp) #기존의 값과 새로운값을 비교해 큰값으로 갱신해줌

lt,rt = 1,largest

while lt <=rt:
    mid =(lt+rt)//2 #mid -> 랜선의 길이
    if Count(mid)>=n: #답이 됨(cnt는 만들수 있는 랜선 그 랜선이 n보다 같거나 크면 답이됨)
        res = mid #답이 될 수 있으니 res변수에 저장해둠
        lt = mid+1
    else: #n개가 안나옴 (길이가 길다)
        rt = mid-1

print(res)

