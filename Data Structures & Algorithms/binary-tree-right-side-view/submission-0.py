# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        right = []
        if not root: 
            return []
        
        queue = deque([root])

        while queue: 
            currLevel = len(queue)

            for n in range(currLevel): 
                node = queue.popleft()
                if n == currLevel -1:
                    right.append(node.val)
                
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return right



        