# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        #check where are p and q
        if not root or not p or not q: 
            return None
               
               
         #if both are on the left side: 
        #call recursion to traverse the left 
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        
        #if both are on the right side
        #call recursion to traverse the right
        elif(min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)

        #if they are on different subtrees, then the answer has to be the root
        else: 
            return root
        
      

        #if both on different subtrees: 
            #the answer is the root 
        
        #if both on right side
            #the answer ir the root
        