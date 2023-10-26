# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Use res as a list instead of directly as an integer, otherwise when we try to access res (as an integer) inside of our method depth(), it will create a local copy there and won't be a global variable anymore. How sick is that! 
        res = [0]
        # Tried using res = 0 instead, and it won't work, you know why now :)

        def depth(root):
            if not root:
                return -1
            
            left = depth(root.left)
            right = depth(root.right)

            res[0] = max(res[0], left + right + 2)

            return 1 + max(left, right)
        
        depth(root)

        return res[0]

        

