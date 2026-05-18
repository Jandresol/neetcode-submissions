class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        ans = 0
        while left < right:
            amount = (right - left) * min(heights[left], heights[right])
            ans = max(amount, ans)
            # Moving the pointer
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return ans

        