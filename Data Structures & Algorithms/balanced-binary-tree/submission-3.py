# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # error - read the question: of EVERY node
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return [True,0]
            left = dfs(root.left)
            right = dfs(root.right)
            height = 1 + max(left[1], right[1])
            if (left[0] and right[0] 
                and abs(left[1] - right[1]) <= 1):
                return [True, height]

            return [False, height]

        return dfs(root)[0]


        