import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
     
        for num in range(k-1): 
            heapq.heappop(maxHeap)


        kth_elem = heapq.heappop(maxHeap)
        return -kth_elem



        