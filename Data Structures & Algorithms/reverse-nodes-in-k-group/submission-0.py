# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy
        while True:
            kth = prevGroup
            n = k
            while kth and n > 0:
                kth = kth.next
                n -=1
            # we're done when we reach the kth
            if not kth:
                break
            nextGroup = kth.next   

            curr = prevGroup.next         
            # prev is what we attach the current node to
            # we want to attach the start of a block to the
            # start of a new block
            prev = nextGroup
            while curr != nextGroup:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            # need to connect tail of previous group to new group

            #tail of rev group
            tmp = prevGroup.next
            # tail of prev group to start of new group
            prevGroup.next = kth
            # tail of prev group is now tail of rev group
            prevGroup = tmp
        return dummy.next
        