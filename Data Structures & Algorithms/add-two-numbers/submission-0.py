# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        '''
        treat this as an addition 
        we are given two reversed lists 
            1
        1   2   3
        4   5   7 
            ^
        5    8    0  
        we have to always take into account a carry, even if there is no carry 
        lists might/might not be of same length 

        '''

        total = ListNode()
        current = total
        carry = 0
        #we want to either have one list or have a carry
        while l1 or l2 or carry:    
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 
            #get values or get zero if we are at end
            #compute total 
            currTotal =val1 +val2 + carry 

            #get rightmost which will be  what we want to add to linked list
            carry = currTotal // 10 
            #get leftmost which will be the carry 
            currentVal = currTotal % 10 
             
            #move to next pointer to allocate on the linked list total
            current.next = ListNode(currentVal)
            current = current.next 

            if l1: 
                l1 = l1.next
            if l2:
                l2 = l2.next 
        
        return total.next

