# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_t(root):
            nonlocal count
            if root is None:
                return None
            res = inorder_t(root.left)
            if res:
                return res
            count += 1
            if count == k:
                return root.val
            res = inorder_t(root.right)
            return res

        count = 0
        res = inorder_t(root)
        if res:
            return res
        return None