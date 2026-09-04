# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import itertools

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        counter = itertools.count()

        heap = [(i.val, next(counter), i) for i in lists if i]
        heapq.heapify(heap)

        dummy = ListNode(0,None)
        current = dummy

        while heap:
            val, x, follow = heapq.heappop(heap)
            current.next = follow
            current = follow
            if current.next:
                heapq.heappush(heap, (current.next.val, next(counter), current.next))

        return dummy.next
