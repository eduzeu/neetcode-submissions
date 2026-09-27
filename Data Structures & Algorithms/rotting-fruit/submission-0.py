from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        rows = len(grid)
        cols = len(grid[0])
        fresh_oranges = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: 
                    q.append((r,c, 0))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
                    
        directions =[(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0

        while q: 
            row, col, minutes = q.popleft()

            for dx, dy in directions: 
                nr = dx + row
                nc = dy + col

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_oranges -=1
                    q.append((nr,nc, minutes + 1))    


        return minutes if fresh_oranges == 0 else -1    
                

                   