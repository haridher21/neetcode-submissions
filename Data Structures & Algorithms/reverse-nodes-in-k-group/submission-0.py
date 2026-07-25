# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        groupHeads = [head]
        headIndex = 0
        counter = 0

        while True:
            counter = 0
            cur = groupHeads[headIndex]
            while cur and counter < k:
                counter += 1
                cur = cur.next

            if not cur and counter < k:
                break

            if counter == k:
                prev, revCur = None, groupHeads[headIndex]
                subCounter = 0
                while subCounter < k:
                    subCounter += 1
                    next = revCur.next
                    revCur.next = prev
                    prev = revCur
                    revCur = next
                
                groupHeads[headIndex] = prev
                if not cur:
                    break
                headIndex += 1
                groupHeads.append(cur)

        for i in range(len(groupHeads) - 1):
            cur = groupHeads[i]
            while cur.next:
                cur = cur.next
            cur.next = groupHeads[i + 1]
        
        return groupHeads[0]
                