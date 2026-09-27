# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

       
        good_nodes = [0]

        def dfs(node, currMax):
            if not node: 
                return 0 
            
            if node.val >= currMax: 
                good_nodes[0] += 1
                currMax = node.val
            
            left = dfs(node.left, currMax)
            right = dfs(node.right, currMax)




        dfs(root, float('-inf')) 
        return good_nodes[0]               

                

        