class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:


        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows): 
            for c in range(r+1, rows): 
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for r in range(rows):
            for c in range(cols//2):
                matrix[r][c], matrix[r][cols-c-1] =  matrix[r][cols-c-1], matrix[r][c]

        