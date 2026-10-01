import heapq
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):


        graph = {i: [] for i in range(1, n+1)}

        for u, v, t in times: 
            graph[u].append((v, t))

        minHeap = []
        visited = set() 
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, (0, k)) 

        while minHeap:

            curr_time, curr_node = heapq.heappop(minHeap)

            if curr_node in visited:
                continue 

            visited.add(curr_node)

            if len(visited) == n: 
                return curr_time 
            
            for nei, next_time in graph[curr_node]: 
                if nei not in visited: 
                    new_time = next_time + curr_time 
                    heapq.heappush(minHeap, (new_time, nei))

        return -1
