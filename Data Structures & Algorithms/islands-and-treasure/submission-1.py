class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()
        q  = deque() 
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: 
                    q.append((r, c, 0)) #row, col, distance 
                    visited.add((r, c))
    
        while q: 
            
            row, col, dist = q.popleft() 

            for dx, dy in directions: 
                nr, nc = dx +row , dy + col
                #check bounds 
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] not in visited and grid[nr][nc] > grid[row][col] and grid[nr][nc] != -1:
                    visited.add((nr, nc))
                    grid[nr][nc] = dist + 1
                    q.append((nr, nc, dist + 1))
        
       

            
            

        