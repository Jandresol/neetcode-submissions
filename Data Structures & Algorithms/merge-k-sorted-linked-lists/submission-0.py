# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge two lists over and over again
        res = None
        if len(lists) == 0:
            return res

        def mergeList(l1, l2):
            # pointer to the start
            dummy = ListNode()
            current = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else: 
                    current.next = l2
                    l2 = l2.next
                # keep moving
                current = current.next
            # remainder
            current.next = l1 or l2
            # return the final list
            return dummy.next

        for i in range(len(lists)):
            res = mergeList(res, lists[i])
        return res