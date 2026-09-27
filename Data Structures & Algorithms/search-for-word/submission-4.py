class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        rows = len(board)
        cols = len(board[0])


        def dfs(r, c, idx):
            #we have reached the word
            if idx == len(word): 
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx] or board[r][c] == "#":
                return False
            
            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            #mark visited
            temp = board[r][c]
            board[r][c] = '#'

            for dx, dy in directions: 
                if dfs(dx + r, dy + c, idx + 1):
                    return True
            
            #unmark for future explorations
            board[r][c] = temp
            return False
            

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
            
        return False


        