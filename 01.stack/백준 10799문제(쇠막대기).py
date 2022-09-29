import sys

s = input()

items=[]   #빈 리스트
cnt = 0;    #토막개수

for i in range(len(s)):
    if s[i] == '(':
        items.append(s[i])
    else: #')' : 닫는괄호 일때
        items.pop()
        if s[i-1] == '(':#레이저일때
            cnt += len(items) #items개수만큼 더해줌
        else: #')' 막대기의 끝점
            cnt += 1

print(cnt)

