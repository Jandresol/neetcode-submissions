# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy for the edge case of removing n = 1
        dummy = ListNode(0, head)
        # You need to put a pointer n steps away from the other
        delete = dummy
        curr = head

        for _ in range(n):
            curr = curr.next

        # bring delete to the position right before n
        while curr:
            curr = curr.next
            delete = delete.next  

        delete.next = delete.next.next
        return dummy.next