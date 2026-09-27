class MinStack:

    # test = []
    # test.push(3) ->  test = [3], min = [3]
    #test.push(2) -> test [3,2], min = [3,2] min = 2 
    #test.pop() = -> test = [3], min = [3]
    #test.top() = -> returns 3
    #test.push(5) = test= [3,5] min [3]
    #test.getMin() -> returns 3
    def __init__(self):
        #use list as data structure 
        self.stack = []
        #keep track of min in list 
        self.minNumber = []
        

    def push(self, val: int) -> None:
        #element must be at top
        self.stack.append(val)
        #update the minimum each time we push 
        if not self.minNumber or val <= self.minNumber[-1]:
            self.minNumber.append(val)


    def pop(self) -> None:
        #check if stack exists
        if self.stack:
        #end of the list
        #[1,2, 3] stack.pop() -> [1, 2]
            popped = self.stack.pop()
        #if we are popping the current min, we have to update
        if popped == self.minNumber[-1]: 
            self.minNumber.pop()
        

    def top(self) -> int:
        #get the number at the end of the list
        #[3,4,5] stack.top() -> returns 5
        if self.stack: 
            last = self.stack[-1]
            return last 
        
    def getMin(self) -> int:
        if self.minNumber:
            return self.minNumber[-1]

        
