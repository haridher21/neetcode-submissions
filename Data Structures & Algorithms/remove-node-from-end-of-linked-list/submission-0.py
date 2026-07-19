# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = 0
        cur = head
        while cur:
            k += 1
            cur = cur.next

        if k < n:
            return head
        if k == n:
            return head.next
        

        cur, prev = head, None
        for _ in range(k - n):
            prev = cur
            cur = cur.next

        prev.next = cur.next
        return head
        
        