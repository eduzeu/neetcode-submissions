import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        #[6,4,3,2,2]
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)


        while len(maxHeap) > 1: 
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)

            diff = abs(x) - abs(y)

            if diff != 0: 
                heapq.heappush(maxHeap, -diff)

        return -maxHeap[0] if maxHeap else 0
        