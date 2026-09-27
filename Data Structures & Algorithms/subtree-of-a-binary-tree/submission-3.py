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

        def sameTree(root, subRoot):
            
            if not root and not subRoot:
                return True
            
            if not root or not subRoot: 
                return False
            
            if root.val != subRoot.val:
                return False
            
            return sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)
        

        def dfs(root, subRoot):
            
            if not root:
                return False

            if root.val == subRoot.val and sameTree(root, subRoot):
                return True
            
            #not same, keep traversing

            left = dfs(root.left, subRoot)
            right = dfs(root.right, subRoot)

            return left or right 
        
        return dfs(root, subRoot)
            

        
        