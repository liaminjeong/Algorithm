class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack =[]   #스택을 사용
        curr = head
        
        while curr:
            stack.append(curr)
            curr = curr.next
        
        dummy = ListNode()
        tail = dummy
        
        while stack: 
            tail.next = stack.pop()
            tail = tail.next
        tail.next = None    #마지막 노드가 None을 가르키도록
        return dummy.next
