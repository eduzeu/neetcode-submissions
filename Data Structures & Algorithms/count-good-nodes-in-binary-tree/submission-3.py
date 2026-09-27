# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0 

        self.good_nodes = 0

        def dfs(node, curr_max): 
            
            if not node: 
                return 
            
            if node.val >= curr_max: 
                self.good_nodes += 1 
            
            if node.left or node.right: 
                curr_max = max(curr_max, node.val)
            
            dfs(node.left, curr_max)
            dfs(node.right, curr_max)
    
        dfs(root, float('-inf'))
        return self.good_nodes

        