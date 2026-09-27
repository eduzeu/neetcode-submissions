class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        q = deque() 
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(r, c): 
            grid[r][c] = "0"
            q.append((r, c))

            while q:

                r, c = q.popleft()

                for dx, dy in directions: 
                    nr, nc = dx + r, dy + c

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1": 
                        q.append((nr, nc)) 
                        grid[nr][nc] = "0"



        islands = 0

        for r in range(rows): 
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands        