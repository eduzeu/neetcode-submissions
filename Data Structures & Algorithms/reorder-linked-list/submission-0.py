# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #part 1, find middle and last element   
        slow, fast = head, head 

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next 
        
        #part 2: reverse second half
        half = slow.next
        slow.next = None
        prev = None 
        while half: 
            temp = half.next
            half.next = prev
            prev = half
            half = temp 
        
        #part 3: insert nodes at right places
        first = head
        sec = prev

        while  sec:
            temp1, temp2 = first.next, sec.next
            first.next = sec
            sec.next = temp1
            first = temp1
            sec = temp2


        