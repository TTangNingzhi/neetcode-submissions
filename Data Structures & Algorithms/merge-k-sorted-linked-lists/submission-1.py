# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i))
        while heap:
            i = heapq.heappop(heap)[1]
            curr.next = lists[i]
            lists[i] = lists[i].next
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
            curr = curr.next
        return dummy.next