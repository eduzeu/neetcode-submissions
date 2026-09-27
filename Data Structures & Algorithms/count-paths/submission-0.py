class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        grid = [[1 for i in range(n)] for j in range(m)]

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                if r == rows -1 or c == cols - 1:
                    continue 
                
                else: 
                    grid[r][c] = grid[r+1][c] + grid[r][c+1]
        
        return grid[0][0]
        
        