# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


        def dfs(node): 
            #base case 1: both in range
            if p.val <= node.val <= q.val or q.val <= node.val <= p.val: 
                return node 

            if node.val < p.val and node.val < q.val:
                return dfs(node.right)
            
            if node.val > q.val and node.val > p.val: 
                return dfs(node.left)
        
        return dfs(root)



        