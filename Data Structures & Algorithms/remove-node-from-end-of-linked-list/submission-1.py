# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        '''
        0 > 1 > 2 > 3 > 4 > null    n = 2
                ^           ^
        '''
        #add an extra node at the beginning 
        left = head
        right = head 

        while n > 0 and right: 
            right = right.next  #arrive at node n - 1
            n -= 1
        
        #move the left to end at n - 1

        if not right: 
            return head.next 
        
        while right and right.next: 
            left = left.next
            right = right.next 
        
        left.next = left.next.next 

        return head

        