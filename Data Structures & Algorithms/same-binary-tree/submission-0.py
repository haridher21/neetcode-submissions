# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        sp, sq = [p], [q]
        while sp and sq:
            popp, popq = sp.pop(), sq.pop()
            if popp is None and popq is not None:
                return False
            if popp is not None and popq is None:
                return False
            if popp is None and popq is None:
                continue
            if popp.val != popq.val:
                return False
            sp.append(popp.left)
            sq.append(popq.left)
            sp.append(popp.right)
            sq.append(popq.right)
        return True
