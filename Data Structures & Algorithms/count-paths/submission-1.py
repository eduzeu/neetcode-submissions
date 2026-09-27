class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        '''
        s
        [21,15,10,6,3,1
         6,5,4,3,2,1
         1,1,1,1,1,1]
                    e
        '''

        grid = [[1] * n for _ in range(m)]
        
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                #skip the bottom and rightmost 
                if r == rows - 1 or c == cols - 1:
                    continue
                else: 
                    grid[r][c] = grid[r+1][c] + grid[r][c+1]

        return grid[0][0]



        