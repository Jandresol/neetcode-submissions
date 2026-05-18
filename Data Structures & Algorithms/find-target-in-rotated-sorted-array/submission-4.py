class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        l, r = 0, len(nums) - 1
        # [4,5,6,7,0,1,2] 
        # [6,7,0,1,2, 3] 

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            # check if you're in the left portion
            if nums[mid] >= nums[l]:
                # if target > mid, search right
                if target > nums[mid]:
                    l = mid + 1
                # if target is less than the left half go right
                elif target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # we're in the right portion
            else:
                # if target < mid, go to the left
                if target < nums[mid]:
                    r = mid - 1
                # if target > right half, go to the left
                elif target > nums[r]:
                    r = mid - 1
                else: 
                    l = mid + 1
        return -1


