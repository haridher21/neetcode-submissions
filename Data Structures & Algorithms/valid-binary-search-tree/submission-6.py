# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def checkValidNode(node, root): #O(H)
            if root is None:
                return False
            if node == root:
                return True
            if node.val == root.val:
                return False
            elif node.val < root.val:
                return checkValidNode(node, root.left)
            else:
                return checkValidNode(node, root.right)

        if root is None:
            return True

        stack = [root.left, root.right]
        while stack: # O(N)
            node = stack.pop()
            if node:
                if not checkValidNode(node, root):
                    return False
                stack.append(node.left)
                stack.append(node.right)
        return True
