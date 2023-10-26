# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # Follow a bottoms-up approach
        # Calculate the max height of the left subtree
        # Calculate the max_height of the right subtree
        # Check if the difference if > 1 and go up from there

        diff = [0]

        def dfs(root):

            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)

            local_diff = abs(left-right)

            if local_diff > 1:
                diff[0] = local_diff
                return diff[0]
            return 1 + (max(left, right))
        
        dfs(root)

        if diff[0] == 0:
            return True
    
        return False
        