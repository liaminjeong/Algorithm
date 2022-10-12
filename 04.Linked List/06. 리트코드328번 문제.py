'''
처음 나의 풀이 생각
      ==> 1) 큐 두개를 만들어서 next값과 next.next 값을 각각의 홀수 큐, 짝수 큐에 넣고 popleft로 붙이려고 했음
      ==> 2) for 문을 돌면서 i%2 를 사용해 하려고 했으나 연결리스트는 len이 없었음
      
풀이
      ==> 홀수 짝수 따로 생각!! 한번에 붙이려고 생각하지 않기
'''

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
        if not head or not head.next or not head.next.next: #엣지케이스 고려
            return head
        
        oddpt = curr = head #홀수 포인터와 curr은 head , 처음을 가리킴
        evenpt = evenhead = head.next 
        #짝수 포인터와 짝수의 시작head는 head의 다음을 가리킴
        
        i = 1 #카운트 변수
        
        while curr: #curr가 있을 때까지
            if i>2 and i%2 !=0: #i가 2보다 크고 홀수 일때 
            #여기서 왜 i가 2보다 크다를 조건으로 줬나 봤더니
            #i=1은 홀수의 head이고 i=2는 짝수의 head
                oddpt.next = curr #홀수의 다음번째를 curr로 주기위해 i는 홀수,짝수head의 i보다 커야함
                oddpt = oddpt.next
            elif i>2 and i%2 ==0: #i가 짝수일때
                evenpt.next = curr
                evenpt = evenpt.next
            curr = curr.next
            i +=1
            
        #curr가 없으면 
        evenpt.next = None  
        # 어차피 마지막은 짝수번째고 짝수번째의 제일마지막은 None을 가리킴
        oddpt.next = evenhead

        return head
