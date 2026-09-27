class Solution:
    def findMin(self, nums: List[int]) -> int:

        minNum = float('inf')
        l = 0 
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                minNum = min(minNum, nums[l])
                break

            mid = (l + r) // 2

            minNum = min(minNum, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        
        return minNum 

        