# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.gc(root, root.val)

    def gc(self, node, limit):
        if node is None:
            return 0
        
        newgc = 0
        if node.val >= limit:
            newgc = 1
            limit = node.val
        
        return newgc + self.gc(node.left, limit) + self.gc(node.right, limit)