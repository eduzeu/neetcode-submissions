class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
         check = set(nums)

         return True if len(check) != len(nums) else False