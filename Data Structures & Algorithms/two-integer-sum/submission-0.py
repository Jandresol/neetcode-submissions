class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)
        for i, n in enumerate(nums):
            diff = target - n
            # Look at previous indices
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[n] = i
        return


