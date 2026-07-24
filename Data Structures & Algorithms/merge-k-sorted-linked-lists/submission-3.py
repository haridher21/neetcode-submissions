# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if not n:
            return None

        mergedHead = merged = ListNode()

        heap = []
        for i in range(n):
            heap.append([lists[i].val, i])
        heapq.heapify(heap)

        while heap:
            popped = heapq.heappop(heap)
            merged.next = ListNode(popped[0])
            merged = merged.next

            if lists[popped[1]].next:
                lists[popped[1]] = lists[popped[1]].next
                heapq.heappush(heap, [lists[popped[1]].val, popped[1]])

        return mergedHead.next