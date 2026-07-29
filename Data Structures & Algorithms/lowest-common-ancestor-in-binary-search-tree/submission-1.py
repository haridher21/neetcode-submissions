# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        small, big = None, None
        if p.val >= q.val:
            small, big = q, p
        else:
            small, big = p, q
        node = root
        while True:
            if small.val == node.val or big.val == node.val:
                return node
            elif small.val < node.val and big.val > node.val:
                return node
            elif small.val < node.val and big.val < node.val:
                node = node.left
            else: #small.val > node.val and big.val > node.val
                node = node.right