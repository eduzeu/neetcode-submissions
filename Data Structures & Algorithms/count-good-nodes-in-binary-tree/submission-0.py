# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

       
        #keep track of max in path 
        currMax=  float('-inf')
        good_nodes = 0
        #perform DFS to explore all nodes in tree
        def dfs(node, currMax):
            nonlocal good_nodes
     
            #base case: empty tree is given
            if not node: 
                return 0 
        
            
            if node.val >= currMax:
                currMax = node.val 
                good_nodes += 1
            

            dfs(node.left, currMax)
            dfs(node.right, currMax)

        dfs(root, currMax)
    
        return good_nodes
                

                

        