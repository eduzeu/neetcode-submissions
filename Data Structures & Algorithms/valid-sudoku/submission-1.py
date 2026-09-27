from collections import defaultdict

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = len(board)
        cols = len(board[0])

        checkCols, checkGrid, checkRows = defaultdict(set),defaultdict(set),defaultdict(set)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == ".":
                    continue 

                if board[row][col] in checkRows[row] or board[row][col] in checkCols[col] or board[row][col]  in checkGrid[row // 3, col // 3]:
                    return False 
                checkRows[row].add(board[row][col])
                checkCols[col].add(board[row][col])
                checkGrid[(row//3, col //3)].add(board[row][col])
    
        return True

