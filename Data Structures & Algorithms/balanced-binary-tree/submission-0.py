# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.balanced = True 

        def dfs(node):
            if not node: 
                return 0 
            
            #compute height of right and left subtree at each node 
            leftSubTree = dfs(node.left)
            rightSubTree= dfs(node.right)

            #check if the current height is balanced 
            if abs(leftSubTree - rightSubTree) > 1:
                self.balanced = False

            return max(leftSubTree, rightSubTree) + 1


        dfs(root) 
        return self.balanced



        

        