# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        length1, length2 = self.getLength(l1), self.getLength(l2)

        longer, shorter = None, None
        if length1 > length2:
            longer, shorter = l1, l2
        else:
            longer, shorter = l2, l1

        head = longer

        carry, prev = 0, None
        while shorter:
            placeSum = longer.val + shorter.val + carry
            longer.val = placeSum % 10
            carry = placeSum // 10
            prev = longer
            longer, shorter = longer.next, shorter.next
        if carry:
            if longer:
                while longer.val == 9:
                    longer.val = 0
                    if longer.next:
                        longer = longer.next
                    else:
                        longer.next = ListNode(1)
                        break
                else:
                    longer.val += 1
            else:
                prev.next = ListNode(1)

        return head

    def getLength(self, cur: Optional[ListNode]) -> int:
        length = 0
        while cur:
            length += 1
            cur = cur.next
        return length
