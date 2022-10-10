class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) ->Optional[ListNode]:
        dummy = ListNode(next=head) #dummy 노드의 다음을 head로 연결한다 
        prev,curr = dummy, head #이전노드(prev)를 dummy 로 현재노드(curr)을 head로 
        
        while curr: #현재노드(curr)가 있을때까지 돈다 즉 head가 있을 때까지 
            nxt = curr.next
            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr
            curr = nxt
        return dummy.next
      
      
#처음 풀어본 풀이     
#         dummy_node = ListNode(next=head)
#         # dummy_node.next = head
        
#         prev_node = dummy_node
#         crnt_node = head
        
#         while crnt_node.next is not None:
#             if crnt_node == val:
#                 prev_node.next = crnt_node.next             
#             else:
#                 prev_node = crnt_node
#             crnt_node = crnt_node.next                
#         return dummy_node.next
      
  
