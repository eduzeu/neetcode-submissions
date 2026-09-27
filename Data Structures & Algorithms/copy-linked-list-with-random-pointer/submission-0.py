"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        dummy = Node(0)
        current_new = dummy
        current_old = head

        mapping = {}


        while current_old: 
            copy = Node(current_old.val)
            mapping[current_old] = copy
            current_new.next = copy

            current_new = current_new.next
            current_old = current_old.next

        current_old = head
        
        while current_old: 
            if current_old.random:
                mapping[current_old].random = mapping[current_old.random]
            current_old = current_old.next

        return dummy.next

        