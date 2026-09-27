from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        #get dimensions 
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        
        for row in range(rows): 
            for col in range(cols): 
                if grid[row][col] == 0:
                    queue.append((row,col))

       # print(queue)
        directions = [(-1,0), (0,1), (0,-1), (1,0)]
        while queue: 
            r, c = queue.popleft() 
           # print(queue, r, c )

            for dx, dy in directions: 
                nr = r + dx
                nc = c + dy 
                if nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] == 2147483647:
                    print(grid[r][c])
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))


                  







        

        
        