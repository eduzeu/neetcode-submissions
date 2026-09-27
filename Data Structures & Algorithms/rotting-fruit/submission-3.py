class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (-1,0), (1,0), (0,-1)] 
        fruits = 0 
        mins = 0 
        q = deque() 


        for r in range(rows):
            for c in range(cols): 
                if grid[r][c] == 2: 
                    q.append((r,c,0)) 
                elif grid[r][c] == 1: 
                    fruits += 1 

        while q: #multisource bfs


            row, col, mins = q.popleft() 

            for dx, dy in directions: 

                nr, nc = dx + row, dy + col

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1: 
                    q.append((nr, nc, mins + 1))
                    grid[nr][nc] = 2 #rot 
                    fruits -= 1 
        

        return mins if fruits == 0 else -1

