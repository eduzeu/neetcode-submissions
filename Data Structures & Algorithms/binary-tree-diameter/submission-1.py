# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #traverse the tree node by node using DFS
        #at each node, we recusively compute the sum of the heights and take the max
        #the value at the end will be the largest distance, therfore the diameter

        self.diameter = 0 

        def sumOfHeights(root): 
            if not root: 
                return 0
            
            sumHeights = 1+ max(sumOfHeights(root.left), sumOfHeights(root.right))
            self.diameter = max(self.diameter,sumOfHeights(root.left) + sumOfHeights(root.right) )
            return sumHeights 
        
        sumOfHeights(root)
        return self.diameter




        