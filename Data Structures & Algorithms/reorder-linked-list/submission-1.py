# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #part 1: find middle and last elements
        slow = fast = head
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        
        #part 2: reverse second half 
        prev = None
        dummy = slow 
        while dummy: 
            nextNode = dummy.next 
            dummy.next = prev
            prev = dummy 
            dummy = nextNode
        
        #part 3: use middle to iterate from there to end and switch pointers
        temp = head
        mid = prev
        
        while mid and mid.next: 
            tmp1, tmp2 = temp.next, mid.next
            temp.next = mid
            mid.next = tmp1
            temp, mid = tmp1, tmp2
         
        

        
      