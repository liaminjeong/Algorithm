import sys
n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort() #오름차순 정렬
lt,rt =0,n-1 # 포인트변수 lt:왼쪽끝 rt:오른쪽끝

while lt<=rt: # lt가 rt보다 커지면 종료
    mid = (lt+rt)//2 #중간값
    if num[mid]==m: 
        print(mid+1) #mid는 index, 0번부터시작. 몇번째냐고 했으니 +1해줌
        break
    elif num[mid] >m:
        rt = mid-1
    else:
        lt = mid+1

