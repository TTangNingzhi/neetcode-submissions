# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = s = ListNode()
        s_prev = None
        while l1 and l2:
            temp = s.val + l1.val + l2.val
            s.val = temp % 10
            s.next = ListNode(val=temp // 10)
            s_prev = s
            s, l1, l2 = s.next, l1.next, l2.next
        r = l1 or l2
        while r:
            temp = s.val + r.val
            s.val = temp % 10
            s.next = ListNode(val=temp // 10)
            s_prev = s
            s, r = s.next, r.next
        if s.val == 0 and s_prev != 0:
            s_prev.next = None
        return head
            