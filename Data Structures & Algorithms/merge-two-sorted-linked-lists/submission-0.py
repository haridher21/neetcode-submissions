# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            smaller, bigger = list1, list2
        else:
            smaller, bigger = list2, list1
        
        head = smaller
        
        while smaller and bigger:
            if smaller.next:
                if smaller.next.val > bigger.val:
                    cur = bigger
                    bigger = bigger.next
                    next = smaller.next
                    smaller.next = cur
                    cur.next = next
                    smaller = cur
                else:
                    smaller = smaller.next
            else:
                smaller.next = bigger
                break

        return head