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
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.random
            curr.random = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = curr.random
            if copy.next:
                copy.random = copy.next.random
            curr = curr.next

        curr = head
        while curr:
            copy = curr.random
            copy.next = curr.next.random if curr.next else None
            curr = curr.next
        
        return head.random if head else None

