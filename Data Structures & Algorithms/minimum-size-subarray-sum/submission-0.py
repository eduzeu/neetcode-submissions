class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        '''
        nums = [2,1,5,1,5,10], target = 10, currSum = 12
                 ^        ^

        approach: sliding window 
        left and right pointers
        keep computing the currrent sum of the subarrays
        if current sum is >= target, then shrink the window and update the distance as 
        long as it's valid 

        time complexity O(n)
        space compleixity O(1)

        '''

        left = 0 
        minDistance = float("inf")
        currSum = 0 

        for right in range(len(nums)): 
            currSum += nums[right]

            while currSum >= target and left <= right: 
                minDistance = min(minDistance, right - left + 1)
                currSum -= nums[left]
                left += 1
                
        
        return minDistance if minDistance != float('inf') else 0






        