class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        res = []

        def check_pacific(r, c, curr_val, visited):

            if r < 0 or c < 0:
                return True

            if (
                r >= rows or c >= cols or
                heights[r][c] > curr_val or
                (r, c) in visited
            ):
                return False

            visited.add((r, c))
            curr_val = heights[r][c]

            if check_pacific(r + 1, c, curr_val, visited):
                return True
            if check_pacific(r - 1, c, curr_val, visited):
                return True
            if check_pacific(r, c + 1, curr_val, visited):
                return True
            if check_pacific(r, c - 1, curr_val, visited):
                return True

            return False

        def check_atlantic(r, c, curr_val, visited):

            if r >= rows or c >= cols:
                return True

            if (
                r < 0 or c < 0 or
                heights[r][c] > curr_val or
                (r, c) in visited
            ):
                return False

            visited.add((r, c))
            curr_val = heights[r][c]

            if check_atlantic(r + 1, c, curr_val, visited):
                return True
            if check_atlantic(r - 1, c, curr_val, visited):
                return True
            if check_atlantic(r, c + 1, curr_val, visited):
                return True
            if check_atlantic(r, c - 1, curr_val, visited):
                return True

            return False

        for r in range(rows):
            for c in range(cols):

                if (
                    check_pacific(r, c, heights[r][c], set())
                    and
                    check_atlantic(r, c, heights[r][c], set())
                ):
                    res.append([r, c])

        return res