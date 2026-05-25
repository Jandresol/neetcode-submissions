class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, lst, total):
            # base case
            if total == target:
                res.append(lst.copy())
                return
            # edge:
            if i >= len(nums) or total > target:
                return

            # include number
            lst.append(nums[i])
            dfs(i, lst, total + nums[i])
            # skip number
            lst.pop()
            dfs(i+1, lst, total)
        dfs(0, [], 0)
        return res



        
        