class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = nums[0]

        store = {}

        for elem in nums: 
            if elem in store: 
                store[elem] += 1
                if store[elem] > store[num]: 
                    num = elem
            else: 
                store[elem] = 1

        return num