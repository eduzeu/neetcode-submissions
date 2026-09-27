class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums) - 1

        for i in range(len(nums)-2,-1,-1): 
            #can we reach the goal index? 
            if nums[i] + i >= goal: 
                goal = i #update goal for curr index 
        
        return True if goal == 0 else False

        