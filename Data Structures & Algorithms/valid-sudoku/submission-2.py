from collections import defaultdict

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = len(board)
        cols = len(board[0])

        rowSet, colSet, boxSet = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(rows):
            for c in range(cols): 
                val = board[r][c] 
                if val == ".":
                    continue
                
                if val in rowSet[r] or val in colSet[c] or val in boxSet[r// 3, c // 3]:
                    return False
                
                rowSet[r].add(val)
                colSet[c].add(val)
                boxSet[(r// 3, c // 3)].add(val)

            
        return True

