# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        paths = []

        def preorder(node, currStr): 
            if not node: 
                return 
            
            currStr += str(node.val)

            if not node.left and not node.right: 
                paths.append(currStr)
                currStr = ''
            else:
                preorder(node.left, currStr)
                preorder(node.right, currStr)
        
        preorder(root, "")
        paths = [int(x) for x in paths]
        return sum(paths)

        