class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head) #dummy에 0을 넣고 next 는 head
        
        # step1 : reach node at position "left"// left노드에 접근하기
        leftPrev,curr = dummy,head #leftPrev는 dummy, curr는 head
        for i in range(left-1): #curr노드가 left노드가 되려면 1번 움직여야함 (left-1번 움직임)
            leftPrev, curr = curr, curr.next
            
        # now curr = "left", leftPrev = "node before left"
        # 현재노드가 left까지 왔음. 
        # step2 : reverse from left to right //left~right까지 역순정렬
        prev = None
        for i in range(right -left+1): #
            tmpNext = curr.next #이동할 다음값 저장
            curr.next = prev 
            prev ,curr = curr, tmpNext
        
        # step2 : update pointer //포인터 변경
        leftPrev.next.next = curr 
        #2에서 5로 연결해야 하는데 현재 2의 위치가 정해져 있지 않음 
        #하지만 1->2 가 현재 연결되어있고 1은 leftPrev노드로 위치가 정해져 있음 
        #따라서 leftPrev의 next #2 next를 현재 curr이 가르키고 있는 5로 연결해줌
        leftPrev.next = prev
        #현재 leftPrev값은 1, leftPrev를 prev가 가리키고 있는 4로 연결해줌
        
        return dummy.next
