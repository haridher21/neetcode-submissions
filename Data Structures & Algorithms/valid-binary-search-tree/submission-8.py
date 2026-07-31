# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder_t(root):
            if root is None:
                return
            inorder_t(root.left)
            inorder.append(root.val)
            inorder_t(root.right)

        inorder = []
        inorder_t(root)
        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i - 1]:
                return False
        return True
