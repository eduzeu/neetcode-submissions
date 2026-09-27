class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.curr_len = 0 
        self.front = None
        self.rear = None
        

    def enQueue(self, value: int) -> bool:
        if self.curr_len >= self.k:
            return False
        
        newNode = ListNode(value)

        if not self.front:  # empty queue
            self.front = newNode
            self.rear = newNode
            newNode.next = newNode  # circular
        else:
            newNode.next = self.front
            self.rear.next = newNode
            self.rear = newNode  # update tail

        self.curr_len += 1
        return True
        

    def deQueue(self) -> bool:
        if not self.front:  # empty
            return False
        
        if self.curr_len == 1:  # only one element
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front  # keep circular link

        self.curr_len -= 1
        return True
        

    def Front(self) -> int:
        return -1 if not self.front else self.front.val

    def Rear(self) -> int:
        return -1 if not self.rear else self.rear.val
        

    def isEmpty(self) -> bool:
        return self.curr_len == 0 
        

    def isFull(self) -> bool:
        return self.curr_len == self.k
