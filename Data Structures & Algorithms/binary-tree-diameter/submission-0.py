# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return max(self.diameter(root)) - 1

    def diameter(self, root: Optional[TreeNode]) -> [int, int]:
        if not root:
            return [0, 0]
        leftDiameter, leftLongest = self.diameter(root.left)
        rightDiameter, rightLongest = self.diameter(root.right)
        return [max(leftDiameter, rightDiameter, 1 + leftLongest + rightLongest), 1 + max(leftLongest, rightLongest)]
