class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        #(enqueuetime, processingtime, index)
        sorted_tasks = sorted([[enqueTime, proccesing, i] for i,  (enqueTime, proccesing) in enumerate(tasks)])

        i = 0 
        minHeap = []
        cpu = []
        time = 0 

        while i < len(sorted_tasks) or minHeap: 

            #build min heap 
            while i < len(sorted_tasks) and sorted_tasks[i][0] <= time: 
                enq, processing, idx = sorted_tasks[i]
                heapq.heappush(minHeap, (processing, idx))
                i += 1
            
            if minHeap: 
                processing, idx = heapq.heappop(minHeap)
                time += processing
                cpu.append(idx)
            
            else: 
                time = sorted_tasks[i][0]


        return cpu