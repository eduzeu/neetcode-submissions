class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        # Handle 1x1 grid case
        if rows == 1 and cols == 1:
            return 0 if obstacleGrid[0][0] == 1 else 1

        # Early exit if start or end is blocked
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
            return 0

        # Step 1: Mark obstacles as -1 (skip start)
        for r in range(rows):
            for c in range(cols):
                if (r != 0 or c != 0) and obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = -1

        # Step 2: Set bottom-right cell
        obstacleGrid[rows-1][cols-1] = 1

        # Step 3: Fill last row (right to left)
        for c in range(cols - 2, -1, -1):
            if obstacleGrid[rows-1][c] == -1:
                continue
            obstacleGrid[rows-1][c] = obstacleGrid[rows-1][c+1] if obstacleGrid[rows-1][c+1] != -1 else 0

        # Step 4: Fill last column (bottom to top)
        for r in range(rows - 2, -1, -1):
            if obstacleGrid[r][cols-1] == -1:
                continue
            obstacleGrid[r][cols-1] = obstacleGrid[r+1][cols-1] if obstacleGrid[r+1][cols-1] != -1 else 0

        # Step 5: Fill the rest from bottom-right to top-left
        for r in range(rows - 2, -1, -1):
            for c in range(cols - 2, -1, -1):
                if obstacleGrid[r][c] == -1:
                    continue
                down = obstacleGrid[r+1][c] if obstacleGrid[r+1][c] != -1 else 0
                right = obstacleGrid[r][c+1] if obstacleGrid[r][c+1] != -1 else 0
                obstacleGrid[r][c] = down + right

        return obstacleGrid[0][0]