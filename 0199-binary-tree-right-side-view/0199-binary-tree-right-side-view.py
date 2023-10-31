# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        if root:
            curr = root
            q = collections.deque()
            q.append(curr)
        else:
            return []

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level[-1])
    
        return result




















        # Start at the root node

        # Check if it has a right node
        # If yes, add it to the list and move to the right node
        # If no, go to the left node, add it to the list and repeat the process.

        # if root:
        #     curr = root
        #     result = [curr.val]
        # else:
        #     return []

        # while curr:

        #     if curr.right:
        #         # print("Right")
        #         result.append(curr.right.val)
        #         curr = curr.right
            
        #     elif curr.left:
        #         # print("Left")
        #         result.append(curr.left.val)
        #         curr = curr.left
        #     else:
        #         break

        #     # print("Result so far: ", result)
            
        # return result

        