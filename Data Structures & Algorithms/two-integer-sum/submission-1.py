class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        compliments = {}

        for i in range(len(nums)):
            
            diff = target - nums[i]

            if diff in compliments: 
                return [compliments[diff], i]
            
            compliments[nums[i]] = i #numer: index
        
    

