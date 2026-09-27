class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        #get dimensions of the matrix
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            #we are out of bounds or the cell to visit is zero/has been visited 
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
                return 0

            areaofCurrentIsland = 1

            directions = [(-1,0), (0,1), (0, -1),(1,0)] #left, up, down, right 
            
            #mark cell as visited 
            grid[row][col] = 0

            for dx, dy in directions: 
                areaofCurrentIsland += dfs(row + dx, col + dy) #explore all possible and valid directions 

            return areaofCurrentIsland
        
        maxArea = 0
        #iterate through matrix
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1: 
                    maxArea = max(maxArea, dfs(row, col))
    
        return maxArea



        