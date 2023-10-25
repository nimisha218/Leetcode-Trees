# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Base Case: If root is None
        if root == None:
            return None
        
        # Swap the left and right sub-trees
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursively make a call to the invertTree function to swap and invert the 
        # left and the right sub-trees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        
        