# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def is_valid(head, k):
            curr = head
            for i in range(k):
                if not curr:
                    return False
                curr = curr.next
            return True

        def reverse(head, k):
            prev, curr = None, head
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev, curr

        dummy = start = ListNode()
        group_end = head
        start.next = group_end
        while True:
            if not is_valid(group_end, k):
                return dummy.next
            prev, curr = reverse(group_end, k)
            start.next = prev
            start = group_end
            group_end = curr
            start.next = group_end
