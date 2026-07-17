# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur1, cur2 = head, head.next if head else None
        while cur1 and cur2 and cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next.next if cur2.next else None
        if cur1 and cur2 and cur1 == cur2:
            return True
        return False