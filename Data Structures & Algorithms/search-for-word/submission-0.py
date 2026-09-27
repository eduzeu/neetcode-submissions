class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        count = 0

        def dfs(row, col, count):
            
            #we have found the word 
            if count == len(word):
                return True 

            #base case: out of bounds, or the letter is not in word 
            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != word[count]:
                return False 
            
            temp = board[row][col] 
            board[row][col] = '#'
            #letter part of sequence and in bounds, explore all possible paths
            directions = [(-1,0), (0,1),(0,-1), (1,0)]

            for dx, dy in directions:  
                if dfs(dx + row, dy + col, count + 1 ):
                    return True 
        
            board[row][col] = temp
            return False

        for row in range(cols): 
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False

        