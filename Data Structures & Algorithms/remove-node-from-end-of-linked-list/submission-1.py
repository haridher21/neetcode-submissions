# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur1 = head
        for _ in range(n):
            if not cur1:
                return head
            cur1 = cur1.next
        
        cur2, prev = head, None
        while cur1:
            cur1 = cur1.next
            prev = cur2
            cur2 = cur2.next
        if prev:
            prev.next = cur2.next
            return head
        return head.next