class Solution:
    def totalNQueens(self, n: int) -> int:

        grid = [["."] * n for _ in range(n)]
        posDiag = set()
        negDiag = set()
        col = set()
        self.solutions = 0

        def backtrack(r):
            if r == n: 
                self.solutions += 1
                return 
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                posDiag.add(r + c)
                negDiag.add(r - c)
                col.add(c)
                grid[r][c] = "Q"
                backtrack(r + 1)

                posDiag.remove(r + c)
                negDiag.remove(r - c)
                col.remove(c)
                grid[r][c] = "."
        
        backtrack(0)
        return self.solutions

        