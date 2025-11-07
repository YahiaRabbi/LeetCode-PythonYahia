"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        while curr:
            if curr.child:
                oldNext = curr.next
                curr.next = self.flatten(curr.child)
                curr.next.prev = curr
                curr.child = None

                while curr.next:
                    curr = curr.next
                curr.next = oldNext


                if oldNext:
                    oldNext.prev = curr

            curr = curr.next
        return head
        
        
        