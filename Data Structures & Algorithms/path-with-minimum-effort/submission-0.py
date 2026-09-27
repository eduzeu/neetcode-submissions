class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        rows, cols = len(heights), len(heights[0])
        visited = set()
        minHeap = [] 
        directions =[(0,1), (0,-1), (1,0), (-1,0)]

        minHeap.append((0, 0, 0)) #diff, row, col 
        heapq.heapify(minHeap)

        while minHeap: 

            diff, row, col = heapq.heappop(minHeap)

            if (row, col) in visited: 

                continue 
            
            visited.add((row, col))

            if (row, col) == (rows -1, cols -1):
                return diff 
            
            for dx, dy in directions: 
                nr, nc = dx + row, dy + col 
                
                #check bounds 
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited: 
                    newDiff = max(diff, abs(heights[row][col] - heights[nr][nc]))

                    heapq.heappush(minHeap, (newDiff, nr, nc))

        return 0 



