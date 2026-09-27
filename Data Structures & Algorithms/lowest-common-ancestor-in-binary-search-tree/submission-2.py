# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(node):
            if node.val == p.val or node.val == q.val: 
                return node 
            
            if p.val < node.val < q.val: #if node is in range
                return node 
            
            if q.val < node.val < p.val: # node is in range
                return node 
            
            if node.val > q.val and node.val > p.val: #go to left
                return dfs(node.left)
            
            if node.val < q.val and node.val < p.val: #go to right
                return dfs(node.right)
        
        return dfs(root)




        