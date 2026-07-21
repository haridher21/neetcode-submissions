"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head
        newHead = Node(head.val)
        prev = newHead
        cur = cur.next

        dn1, dn2 = {}, []
        dn1[head] = 0
        dn2.append(newHead)
        index = 1
        while cur:
            newNode = Node(cur.val)
            prev.next = newNode
            prev = newNode
            dn1[cur] = index
            dn2.append(newNode)
            index += 1
            cur = cur.next

        cur = head
        cur2 = newHead
        while cur:
            if not cur.random:
                cur2.random = None
            else:
                cur2.random = dn2[dn1[cur.random]]
            cur = cur.next
            cur2 = cur2.next
        return newHead
        

        
