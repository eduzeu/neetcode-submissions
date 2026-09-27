class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        nums = set(nums)
        max_sequence = 0 


        for num in nums: 

            sequence = 1 
            temp_num = num

            while temp_num - 1 in nums: 
                sequence += 1 
                temp_num -= 1 
            
            max_sequence = max(max_sequence, sequence) 
        
        return max_sequence
        