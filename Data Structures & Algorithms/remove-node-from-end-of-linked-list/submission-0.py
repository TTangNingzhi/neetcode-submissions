# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, second, prev = head, head, None
        for i in range(n):
            first = first.next
        while first:
            first = first.next
            prev = second
            second = second.next
        if prev:
            prev.next = second.next
            return head
        else:
            return head.next