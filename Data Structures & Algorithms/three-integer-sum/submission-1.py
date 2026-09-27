class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplets = []
        nums.sort()


        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            
            l, r = i+1, len(nums)-1

            while l < r: 
                 
                triplet = nums[i] + nums[l] + nums[r] 

                if triplet == 0: 
                    triplets.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                    while r > l and nums[r] == nums[r+1]:
                        r -= 1

                elif triplet > 0: 
                    r -= 1
                else: 
                    l+= 1
        return triplets      

        