class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:


        rows = len(matrix)
        cols = len(matrix[0])

        #generate matrix of 0's
        paths = [[0] * cols for _ in range(rows)]

        print(paths)

        def dfs(r, c):
            #base base: has been explored
            if paths[r][c] != 0: 
                return paths[r][c]
            
            maxPath = 1

            directions = [(0,1), (0,-1), (1,0), (-1,0)]


            for dx, dy in directions: 
                nr = dx + r
                nc = dy + c

                #check in bounds
                if  0 <= nr < rows and 0 <= nc < cols and matrix[r][c] < matrix[nr][nc]:
                    maxPath = max(maxPath, 1+ dfs(nr, nc))
            
            paths[r][c] = maxPath 

            return maxPath 

        path = 0
        for r in range(rows):
            for c in range(cols):
                path = max(path, dfs(r,c))

        return path


        