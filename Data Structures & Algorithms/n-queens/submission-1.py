class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]: 



        grid = [['.'] * n for _ in range(n)]
        negDiag = set()
        cols = set()
        posDiag = set() 
        ans = [] 

        def backtrack(i): 
            if i == n: 
                copy = ["".join(row) for row in grid]
                ans.append(copy)
                return 
            
            for c in range(n): 
                if c in cols or (c + i) in posDiag or (i - c) in negDiag: 
                    continue
                
                cols.add(c)
                posDiag.add(c + i)
                negDiag.add(i - c)
                grid[i][c] = "Q"

                backtrack(i+1)
                cols.remove(c)
                posDiag.remove(c + i)
                negDiag.remove(i - c)
                grid[i][c] = "."
        
        backtrack(0)
        return ans



        