# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        temp = head
        if not head:
            return None
        post = head.next
        while temp:
            temp.next = prev
            prev = temp
            temp = post
            if temp and temp.next:
                post = temp.next
            else:
                post = None

        return prev


        