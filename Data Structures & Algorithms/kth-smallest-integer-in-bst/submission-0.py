# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_t(root):
            if root is None:
                return
            inorder_t(root.left)
            inorder.append(root.val)
            inorder_t(root.right)

        inorder = []
        inorder_t(root)
        return inorder[k - 1]