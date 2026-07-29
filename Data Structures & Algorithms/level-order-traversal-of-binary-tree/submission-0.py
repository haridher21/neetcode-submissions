# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        output = []
        while stack:
            n = len(stack)
            cur_level, next_level = [], []
            for i in range(n):
                node = stack.pop()
                cur_level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            stack = next_level[::-1]
            output.append(cur_level)
        return output
            