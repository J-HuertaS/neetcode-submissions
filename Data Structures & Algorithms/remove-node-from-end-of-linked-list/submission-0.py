# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # invertir lista
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        # invertir la lista y eliminar el n-th elemento
        counter = 1
        current = prev
        prev = None
        while current:
            # verificar si es el n-th elemento
            if counter == n:
                temp = current.next
                current.next = None
                current = temp
                counter += 1
                continue

            temp = current.next
            current.next = prev
            prev = current
            current = temp
            counter += 1

        return prev

        

        