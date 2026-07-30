# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        gnc = 0
        stack = [[root, root.val - 1]]
        while stack:
            node, limit = stack.pop()
            if node:
                # print(node.val, limit)
                if node.val >= limit:
                    gnc += 1
                    limit = node.val
                stack.append([node.left, limit])
                stack.append([node.right, limit])
        return gnc