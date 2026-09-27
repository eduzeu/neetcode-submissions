from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        q = deque()
        output = []

        for i in range(len(nums)):

            #we don't need the index
            if q and q[0] < i - k + 1:
                q.popleft()
            
            #update the max
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            
            q.append(i)

            #we are at k 
            if i >= k- 1: 
                output.append(nums[q[0]])
        
        return output