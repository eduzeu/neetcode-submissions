class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):

            if c < 0 or r < 0 or r == rows or c == cols or board[r][c] != 'O':
                return 
            
            board[r][c] = '#'

            directions = [(-1,0), (0,1), (1,0), (0,-1)]

            for dx, dy in directions: 
                dfs(r+ dx, dy+ c)
        
        #capture unsurrounded regions (O > #)
        for row in range(rows):
            for col in range(cols):
                if (board[row][col] == 'O' and (row in [0, rows-1] or col in [0, cols- 1])):
                    dfs(row, col)
        
        #capture surrounded regions (O > X)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
        
        #uncapture unsurorunded regions (# > X)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == '#':
                    board[row][col] = 'O'