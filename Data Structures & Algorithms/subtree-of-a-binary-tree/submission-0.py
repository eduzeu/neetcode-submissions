# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        #traverse the tree using DFS 
        #at each node, we check its subtrees and compare it to the subroot 
        #if we find a subtree that is equal to subroot based on the node passed, return true
        #at the end of traversal, return false. Nothing found 

        def sameTree(node, subRoot):
            if not node and not subRoot:
                return True 
            if not node or not subRoot: 
                return False

            if node.val != subRoot.val: 
                return False

            left = sameTree(node.left, subRoot.left)
            right = sameTree(node.right, subRoot.right)

            return left and right 

        def dfs(node):
            if not node: 
                return False
            if sameTree(node, subRoot):
                return True

            left = dfs(node.left) 
            right = dfs(node.right)

            return right or left
        
        return dfs(root)

        
        