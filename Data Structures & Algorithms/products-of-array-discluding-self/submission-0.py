class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = suffix = 1
        # Running product [1, 1, 2, 8]
        for i in range (len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # Backwards product [48, 24, 6, 1]
        for i in range (len(nums)-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res



        