# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # We can do pre-order traversal and keep a tab of all the visited nodes in a list
        # Or post-order might work too
        # Inorder too lol

        def inorder(root):

            if not root:
                order.append("Null")
                return
            if root:
                order.append(root.val)
            
            inorder(root.left)
            inorder(root.right)

        order = []
        inorder(p)
        p_order = order
        order = []
        inorder(q)
        q_order = order

        if p_order == q_order:
            return True
        else:
            return False
    