# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        # find the second half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # beginning of the second half of the list
        second = slow.next
        # split the list
        prev = slow.next = None

        # reverse second
        while second:
            temp = second.next
            second.next = prev
            prev = second
            # move pointer
            second = temp
        
        # move second from null to the head of reversed list
        second = prev
        
        while first and second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        