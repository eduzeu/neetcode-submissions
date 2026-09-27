class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        sequence = 0
        for i in range(len(nums)):
            #start of a sequence
            if nums[i] - 1 not in check:
                currLen = 1
                nextNumber = nums[i] + 1 
                #count our sequence 
                while nextNumber in check: 
                    currLen += 1
                    nextNumber += 1
                sequence = max(sequence,currLen )
    
        return sequence 

