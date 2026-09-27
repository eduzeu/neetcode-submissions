import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num: int) -> None:

        if not self.maxHeap and not self.minHeap: 
            heapq.heappush(self.maxHeap, -num)
        else:
            if -self.maxHeap[0] < num:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, -num)
        
        #balance
        if len(self.maxHeap) > len(self.minHeap) +1:
            lower = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, lower)
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            upper = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -upper)
    


    def findMedian(self) -> float:
        maxdist, mindist = len(self.maxHeap), len(self.minHeap)

        if (maxdist + mindist) % 2 == 0: 
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            if maxdist > mindist:
                return -self.maxHeap[0]
            else: 
                return self.minHeap[0]    
        