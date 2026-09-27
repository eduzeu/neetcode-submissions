class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sums = {}

        for i in range(len(nums)):
            
            complement = target - nums[i]
            if complement in sums: 
                return [sums[complement], i]

            sums[nums[i]] = i
        

