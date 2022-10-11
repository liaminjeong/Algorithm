class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_node = head    #한번에 두칸씩 이동
        slow_node = head    #한번에 한칸씩 이동
        
        while fast_node and fast_node.next: #fast노드가 있고 fast노드의 next가 있으면
            fast_node = fast_node.next.next
            slow_node = slow_node.next
      #만약 fast_node가 None이면 slow_node가 가운데가 됨
        return slow_node
