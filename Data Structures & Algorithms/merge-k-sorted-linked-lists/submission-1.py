# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = final = ListNode()
        n = len(lists)

        while True:
            allNone = True
            smallest, smallInd = float("inf"), 0
            for i in range(n):
                if lists[i] and lists[i].val < smallest:
                    allNone = False
                    smallest = lists[i].val
                    smallInd = i

            if allNone:
                return head.next

            final.next = ListNode(smallest)
            final = final.next
            lists[smallInd] = lists[smallInd].next
            