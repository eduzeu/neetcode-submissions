from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {} 
        #create array of empty lists 
        freqs = [[] for i in range(len(nums) + 1)]
        
        #get numbers frequency 
        for n in nums: 
            if n not in count: 
                count[n] = 0
            else:
                count[n] += 1
            
        for n, c in count.items(): 
            freqs[c].append(n) #c is the times n number appears
        
        ans = []
        #get top k elements
        for i in range(len(nums)-1,-1,-1): 
            for n in freqs[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans

    

        


        