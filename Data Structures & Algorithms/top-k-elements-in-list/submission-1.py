class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = {}
        ans = []
        #count frequencies 
        for num in nums: 
            freqs[num] = freqs.get(num, 0) + 1
        
        #create array of indexes
        indexes = [[] for i in range(len(nums) + 1)]

        #append frequencies to the array
        for n, f in freqs.items(): 
            indexes[f].append(n) #append number
        
        for i in range(len(indexes) -1,-1,-1):
            for num in indexes[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
            
 
        


        