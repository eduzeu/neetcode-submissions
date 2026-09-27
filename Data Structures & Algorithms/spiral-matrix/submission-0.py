from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        spiral = []
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        
        while len(spiral) < rows * cols:
            # Move right
            for c in range(left, right + 1):
                spiral.append(matrix[top][c])
            top += 1  # Move the top boundary down
            
            # Move down
            for r in range(top, bottom + 1):
                spiral.append(matrix[r][right])
            right -= 1  # Move the right boundary left
            
            if top <= bottom:
                # Move left
                for c in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][c])
                bottom -= 1  # Move the bottom boundary up
            
            if left <= right:
                # Move up
                for r in range(bottom, top - 1, -1):
                    spiral.append(matrix[r][left])
                left += 1  # Move the left boundary right
        
        return spiral
