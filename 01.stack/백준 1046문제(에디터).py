import sys

items =list(input())   #초기 입력된 문자열
str= []  #빈 리스트
n = int(input())   #문자열길이
# aaa
for i in range(n):
    val = list(sys.stdin.readline().split())
    if val[0] == 'L':
        if items:  #items 값이 있으면 
            str.append(items.pop())
    elif val[0] == 'D':
        if str: #str 값이 있으면 
            items.append(str.pop())
    elif val[0] == 'B':
        if items:    #items 값이 있으면 
            items.pop()
    else:
        items.append(val[1])

items.extend(reversed(str))     
# for _ in range(len(str)):
#     items.append(str.pop())
print(''.join(items))

#reverse(), reversed()
#1) 리스트의 값 순서를 거꾸로 뒤집는다
#2) 반환되느냐 안되느냐의 차이

#reverse() :  아무런 값도 반환하진 않음(단순히 list섞어줌)
#reversed() : 리스트를 반환함(내장함수,list에서 제공하는 함수 x)

#리스트에 새로운 원소를 추가하는 방법
#append, extend
#append : 리스트 끝에 x 1개넣는다
#extend : 리스트 끝에 ()안의 모든 항목을 넣는다 
