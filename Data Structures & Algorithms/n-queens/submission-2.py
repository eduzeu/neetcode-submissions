from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        negDiag = set()
        posDiag = set()
        cols = set()
        grid = [['.'] * n for _ in range(n)]
        queens = []

        def backtrack(r):
            if r == n:
                queens.append([''.join(row) for row in grid])
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                grid[r][c] = "Q"
                posDiag.add(r + c)
                negDiag.add(r - c)
                cols.add(c)

                backtrack(r + 1)

                grid[r][c] = "."
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                cols.remove(c)

        backtrack(0)
        return queens