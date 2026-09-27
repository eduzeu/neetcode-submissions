class FreqStack:

    def __init__(self):
        self.groups = defaultdict(list)
        self.freqs = defaultdict(int)
        self.max_freq = 0
        

    def push(self, val: int) -> None:
        #count frequency 
        self.freqs[val] = self.freqs.get(val, 0 ) + 1 
        #map freq to val 
        self.groups[self.freqs[val]].append(val)
        #update max 
        self.max_freq = max(self.max_freq, self.freqs[val])


    def pop(self) -> int:
        val = self.groups[self.max_freq].pop()
        self.freqs[val] -= 1 

        if not self.groups[self.max_freq]:
            self.max_freq -= 1
        
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()