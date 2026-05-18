"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyList = {None : None}

        curr = head
        while curr:
            value = Node(curr.val)
            copyList[curr] = value
            curr = curr.next

        curr = head
        while curr:
            copy = copyList[curr]
            copy.next = copyList[curr.next]
            copy.random = copyList[curr.random]
            curr = curr.next
        return copyList[head]


        