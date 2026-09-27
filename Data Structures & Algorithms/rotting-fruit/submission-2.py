class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        q = deque() 
        directions = [(0,-1), (0,1), (1,0), (-1,0)]
        fruits = 0 
        mins = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols): 
                if grid[r][c] == 1: 
                    fruits += 1
                elif grid[r][c] == 2: 
                    q.append((r,c, 0)) #,row, col, mins 
        

        while q: 

            row, col, mins = q.popleft() 

            
            for dx, dy in directions: 
                nr, nc = dx + row, dy + col

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1: 
                    grid[nr][nc] = 2 #rot fruit
                    q.append((nr, nc, mins + 1))
                    fruits -= 1

        
        return mins if fruits == 0 else -1

