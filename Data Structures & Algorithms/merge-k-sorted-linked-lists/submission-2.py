# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None

        mergedHead = ListNode()
        mergedHead.next = lists[0]

        for i in range(1, n):
            first = mergedHead.next
            second = lists[i]
            merged = mergedHead = ListNode()

            while first and second:
                if first.val < second.val:
                    merged.next = first
                    first = first.next
                else:
                    merged.next = second
                    second = second.next
                merged = merged.next
            
            if first:
                merged.next = first
            else:
                merged.next = second


        return mergedHead.next