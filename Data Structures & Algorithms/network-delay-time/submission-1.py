import heapq
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):

        graph = defaultdict(list)

        for u, v, w in times: 
            graph[u].append((v, w))
        
        minHeap = [] 
        visited = set() 

        minHeap.append([0, k])
        heapq.heapify(minHeap)

        while minHeap: 

            curr_time, curr_node = heapq.heappop(minHeap)

            if curr_node in visited:
                continue 
            
            visited.add(curr_node)

            # Check AFTER adding the node
            if len(visited) == n: 
                return curr_time
            
            for v1, w1 in graph[curr_node]:
                if v1 not in visited: 
                    heapq.heappush(minHeap, (curr_time + w1, v1))
        
        return -1