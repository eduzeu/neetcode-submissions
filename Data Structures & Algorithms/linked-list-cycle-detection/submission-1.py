# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        '''
        1   2   3   4
        ^
        ^   
        '''

        #if we use a slow pointer and a fast pointer, then we know the fast will 
        #eventually reach the slow

        #iterate through the list 

        slow = head
        fast = head 

        while fast and fast.next: 

            #update pointers
            slow = slow.next 
            fast = fast.next.next 

            if slow== fast:
                return True 
        
        
        return False 
            