class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        #get dimensions of the matrix
        rows = len(grid)
        cols = len(grid[0])

        def dfs (r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0: 
                return 0
            
            grid[r][c] = 0
            area = 1
            directions = [(-1,0), (0,1), (1,0), (0,-1)]

            for dx, dy in directions: 
                area += dfs(dx + r, dy + c)
                
            
            return area 
        
        maxArea = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1: 
                    maxArea = max(dfs(row, col), maxArea) 
            
        return maxArea
                    



        