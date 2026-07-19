# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        nodes = []
        cur = head
        while cur:
            n += 1
            nodes.append(cur)
            cur = cur.next

        if n < 3:
            return

        if n % 2 == 0:
            for i in range((n // 2) - 1):
                nodes[i].next = nodes[n - i - 1]
                nodes[n - i - 1].next = nodes[i + 1]
                print(nodes[i].val, nodes[n - i - 1].val, nodes[i + 1].val)
            nodes[(n // 2) - 1].next = nodes[n // 2]
            nodes[n // 2].next = None
        else:
            for i in range(n // 2):
                nodes[i].next = nodes[n - i - 1]
                nodes[n - i - 1].next = nodes[i + 1]
                print(nodes[i].val, nodes[n - i - 1].val, nodes[i + 1].val)
            nodes[(n // 2) + 1].next = nodes[n // 2]
            nodes[n // 2].next = None
