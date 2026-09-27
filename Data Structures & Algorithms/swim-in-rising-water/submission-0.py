import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        N = len(grid)
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        minH = [[grid[0][0], 0, 0]] #(time, r, c)
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        visit.add((0,0))
        
        while minH: 
            t, r, c = heapq.heappop(minH)

            if r == N -1 and c == N -1:
                return t

            for dx, dy in directions: 
                nr, nc = dx + r, dy + c

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc ) not in visit: 
                    visit.add((nr, nc ))
                    heapq.heappush(minH, [max(t, grid[nr][nc]), nr, nc])
        