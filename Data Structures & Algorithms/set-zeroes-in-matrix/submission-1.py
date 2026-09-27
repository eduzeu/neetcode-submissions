class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = len(matrix)
        cols = len(matrix[0])

        def modify_rows_cols(r,c): 
            #go left
            left = c - 1
            while left >= 0:
                if matrix[r][left] != 0:
                    matrix[r][left] = "#"
                left -= 1
            
            #go right 
            right = c + 1
            while right < cols: 
                if matrix[r][right] != 0:
                    matrix[r][right] = "#"
                right += 1
            
            #go down 
            down = r + 1
            while down < rows: 
                if matrix[down][c] != 0:
                    matrix[down][c] = "#"
                down += 1
            
            #go up
            up = r - 1
            while up >= 0: 
                if matrix[up][c] != 0:
                    matrix[up][c] = "#"
                up -= 1

        for r in range(rows):
            for c in range(cols): 
                if matrix[r][c] == 0: 
                    modify_rows_cols(r,c)

        #print(matrix)
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "#":
                    matrix[r][c] = 0
            



        
        