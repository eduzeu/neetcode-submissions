class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        result = []

        def dfs(row, col, visit): 

            if row < 0 or col < 0 or row >= rows or col >= cols or (row, col) in visit: 
                return 
            
            visit.add((row, col))
            directions = [(-1,0), (0,1), (0,-1), (1,0)]

            for dx, dy in directions: 

                new_row = dx + row
                new_col = dy + col 

                if 0 <= new_row < rows and 0 <= new_col < cols and heights[new_row][new_col] >= heights[row][col]:
                    dfs(new_row, new_col, visit)
        

        atlantic = set()
        pacific = set()
        
        for col in range(cols):
            dfs(0, col, pacific) #top 
            dfs(rows - 1, col,  atlantic)#bottom
        
        for row in range(rows):
            dfs(row, 0, pacific) #left
            dfs(row, cols -1, atlantic) #right

        for row in range(rows):
            for col in range(cols):
                if (row, col) in atlantic and (row, col)  in pacific: 
                    result.append([row, col])

        return result        