class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if num > 0:
                break
            left = i+1
            right = len(nums)-1
            while left < right:
                threesum = num + nums[left] + nums[right]
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Need to skip over repeated numbers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res



        