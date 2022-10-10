'''
>>>>나의 실수......
1) output리스트까지 3개의 list로 생각하지 않고 2개의 리스트로 생각함 
그래서 초기에 위치를 표시해줄 n1과 n2변수를 생성함 
    dummy = ListNode() 
    tail = dummy 
    위의 빈 리스트에서 새롭게 list1과 list2에 있는 값을 연결하고 기존의 list1과 list2는 연결된 값 지운 다음 값으로 놓으면 되는데 그렇게 생각하지 못했음
'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        #out리스트 만든다
        dummy = ListNode() #아무것도 없는 dummy node
        tail = dummy    #tail node 자기 자신 가르킨다
        
        while list1 and list2: #list1과 list2가 not None 일때까지돈다 
            if list1.val < list2.val:#list1의 val이 list2의 val보다 작으면 
                tail.next = list1 #dummy 다음을 list1으로 연결한다
                list1 = list1.next #주어진 list1을 비교한 값 다음값의 list로 만든다 
            else:
                tail.next = list2
                list2  = list2.next
            tail = tail.next #tail의 위치를 tail.next값으로 옮겨준다 
        
        #어느 한쪽의 리스트가 비어있는 경우 고려(길이가 다른경우)
        if list1: #list1이 있으면 
            tail.next = list1
        elif list2:#list2가 있으면
            tail.next = list2
        
        return dummy.next
      
# 처음 푼 풀이  
# dummy = ListNode(0)
# n1 = list1.val
# n2 = list2.val
# while list1 or list2:
#     if n1 <= n2:
#         dummy.next = n1
#         n1 = n1.next
#     else:
#         n1.prev.next = n2
#         n2 = n2.next
# return dummy.next
        
