class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, lst, total):
            if total == target:
                res.append(lst.copy())
                return

            if i >= len(candidates) or total > target:
                return

            # include candidates[i]
            lst.append(candidates[i])
            dfs(i + 1, lst, total + candidates[i])
            lst.pop()

            # skip candidates[i] and all duplicates of it
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, lst, total)

        dfs(0, [], 0)
        return res