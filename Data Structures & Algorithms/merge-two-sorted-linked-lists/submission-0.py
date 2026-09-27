# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode() #dummy node to keep track of head 
        current = head 
        while list1 or list2: 
            if list1 and list2: 
                if list1.val > list2.val: 
                    current.next = list2 #add list2.val 
                    list2 = list2.next #move list2 pointer to next 
                
                elif list1.val < list2.val:
                    current.next= list1#add list1.val
                    list1 = list1.next#move list2 pointer to next 
                else:
                    #they are equal, move any 
                    #list1 moves to next 
                    current.next = list1
                    list1 = list1.next 
            elif list1: #list2 is done
                current.next = list1
                break
            elif list2: 
                current.next = list2
                break
            
            current = current.next


        return head.next