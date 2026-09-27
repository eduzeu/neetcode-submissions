# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #edge case
        if not root: 
            return []
        #traversal list by level 
        levelOrder = []

        #BFS to visit the tree by levels 
        def bfs(start, traversal):
            #queue to iterate
            queue = deque([start])

            while queue: 
                #check leftmost 
                level = len(queue)
                nodes = []
                
                for i in range(level):
                    node = queue.popleft()
                    nodes.append(node.val)
                #if not in set, add

                    if node.left: 
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                traversal.append(nodes)

            return traversal 

            #bfs on nodes 
        bfs(root, levelOrder) 

        return levelOrder



        