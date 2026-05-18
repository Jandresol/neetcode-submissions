"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #  run a DFS
        # Create a hash table to keep track of what's cloned
        # node -> node
        cloneHash = {}
        res = []
        # for neighbors in neighbor
        def dfs(node):
            if node in cloneHash:
                return cloneHash[node]
            if node:
                copy = Node(node.val)
                cloneHash[node] = copy

                for n in node.neighbors:
                    copy.neighbors.append(dfs(n))
                return copy
        return dfs(node)

                




        