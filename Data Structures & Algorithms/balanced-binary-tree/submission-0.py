# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.getHeight(root)[0]

    def getHeight(self, root):
        if not root:
            return (True, 0)

        lb, lh = self.getHeight(root.left)
        rb, rh = self.getHeight(root.right)

        if not lb or not rb:
            return (False, -1)

        if abs(lh - rh) > 1:
            return (False, -1)

        return (True, 1 + max(lh, rh))
