class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Monotonically Decreasing Queue
        # Want to remove from the beginning in O(1) time (FIFO)
        result = []
        queue = collections.deque() # index
        l = r = 0

        while r < len(nums):
            # Pop smaller values
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            # Remove left value from window if out of bounds
            if l > queue[0]:
                queue.popleft()

            # For each window iteration append leftmost value (max)
            if (r+1) >= k:
                result.append(nums[queue[0]])
                l+=1
            r+=1
        return result
