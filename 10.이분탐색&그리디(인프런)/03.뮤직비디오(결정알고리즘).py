import sys
def Count(capacity): #dvd몇장이 필요한가 return하는 함수
    cnt = 1
    hap = 0
    for x in sing:
        if hap+x > capacity: #x곡은 현재 dvd에 녹음할 수 없다
            #용량초과 
            cnt+=1
            hap = x #새로운 dvd에 무조건 x노래를 넣는다
        else: # 현재곡 저장가능
            hap+=x
    return cnt


n,m = map(int,input().split())
sing = list(map(int,input().split()))
maxx = max(sing) #노래들 중 가장 큰 값
lt,rt = 1,sum(sing)
res = 0

while lt<=rt:
    mid = (lt+rt)//2
    if mid>=maxx and Count(mid)<=m: 
        # mid>=maxx :: 노래 중 가장 긴 노래보다는 dvd하나의 용량이 커야한다 
        # 한 곡은 무조건 들어가야 하니까 (한 곡을 쪼갤 수 없으니)
        res = mid
        rt = mid-1
    else: #용량이 작아서 더 큰게 필요한것 
        lt = mid+1
print(res)

