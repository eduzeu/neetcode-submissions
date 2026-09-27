class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        l = max(nums)
        r = sum(nums)
        largest_sum = 0

        while l <= r: 

            m = (l + r) // 2

            can_split = True #count if we can split exactly k times 
            currSum = 0 
            times = 1

            for num in nums:
                #split current subarray
                if currSum + num > m:
                    times += 1
                    currSum = 0 #reset

                currSum += num 
              
                if times  > k : #we can't split anymore
                    can_split = False
                    break 
            
            if not can_split: 
                l = m + 1
            else: 
                r = m - 1
                largest_sum = m

        return largest_sum 

        