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
        dummy = new = Node(0)
        mapping = {}
        index_mapping = {}
        index = 0
        while curr:
            new.next = Node(curr.val)
            new = new.next
            mapping[index] = new
            index_mapping[curr] = index
            curr = curr.next
            index += 1
        curr = head
        new = dummy.next
        index = 0
        while curr:
            if curr.random:
                new.random = mapping[index_mapping[curr.random]]
            new = new.next
            curr = curr.next
            index += 1
        return dummy.next