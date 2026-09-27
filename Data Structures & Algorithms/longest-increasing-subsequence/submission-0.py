class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        #to solve this problem, we need to: 
        #initialize 1d array with all ones first

        longest = [1] * len(nums)
        #iterate from the end 
        for i in range(len(nums) -1,-1,-1):
            #check all numbers to the right for the subsequence
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]: #subsequence is valid
                    longest[i] = max(longest[i], 1+ longest[j]) #choose to stay or to include 
        
        return max(longest)



         
        #return max

        
        