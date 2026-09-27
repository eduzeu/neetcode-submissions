class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):

            #check if we are out of bounds or that grid[r][c] is not a 0 
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == '0':
                return False 
            
            directions = [(-1,0), (0,1), (0,-1), (1,0)] #left up down and right 
            
            #make sure we keep track of visited cells
            #mark cell as visited
            grid[row][col] = '0'
            
            #call dfs in all directions 
            for dx, dy in directions: 
                dfs(row + dx, col + dy)
        
            return True 

        numberOfIslands= 0 
        for row in range(rows): 
            for col in range(cols):
                if grid[row][col] == '1':
                    if dfs(row, col) == True: #island exists
                        numberOfIslands += 1

        return numberOfIslands 

            
        