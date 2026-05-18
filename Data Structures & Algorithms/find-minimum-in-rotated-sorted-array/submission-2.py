class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 345612
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # Sorted portion, move to the right
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Could be the minimum
                right = mid 
        return nums[left]


        