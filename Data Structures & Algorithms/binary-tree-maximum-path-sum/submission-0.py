# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def maxPath(root):
            if root is None:
                return [float("-inf"), float("-inf")]
            
            leftMax = maxPath(root.left)
            rightMax = maxPath(root.right)
            maxSubtreeWithCurrentNode = max(root.val, leftMax[0] + root.val, rightMax[0] + root.val)
            overAllMax = max(leftMax[1], rightMax[1], maxSubtreeWithCurrentNode, root.val + leftMax[0] + rightMax[0])
            return [maxSubtreeWithCurrentNode, overAllMax]

        return maxPath(root)[1]