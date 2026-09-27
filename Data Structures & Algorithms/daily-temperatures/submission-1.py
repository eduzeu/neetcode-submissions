class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temps = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            #keep stack in decreasing order
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                temps[prev] = i - prev

            stack.append(i)
                
            
        

        return temps 




        
