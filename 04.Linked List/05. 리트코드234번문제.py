class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q:Deque = collections.deque()
            
        curr = head
        
        while curr:
            q.append(curr.val)
            curr = curr.next
            
        while len(q) > 1: #len(q)가 1보다 작으면(즉, 0이면 나감)
            if q.popleft() != q.pop(): #왼쪽pop과 오른쪽 pop이 같지 않으면 어차피 false
                return False
        return True #0이면 앞뒤 같은것
