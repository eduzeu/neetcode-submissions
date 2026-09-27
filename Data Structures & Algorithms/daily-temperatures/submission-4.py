class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temps = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):


            while stack and stack[-1][0] < temperatures[i]:
                temp, idx = stack.pop()
                new_idx = i - idx
                temps[idx] = new_idx

            
            stack.append([temperatures[i], i])


        
        return temps