class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        rows, cols = len(grid), len(grid[0])
        directions = [(-1,0), (1,00), (0,-1), (0,1)]
        q = deque() 

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 0: 
                    q.append((r, c, 0))

        visited = set()

        while q: 

            row, col, dist = q.popleft()

            for dx, dy in directions: 

                nr, nc = dx + row, dy +col 

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > grid[row][col] and grid[nr][nc] != -1 and (nr, nc) not in visited:  
                    q.append((nr, nc, dist + 1))
                    grid[nr][nc] = dist + 1
                    visited.add((nr, nc))



                    