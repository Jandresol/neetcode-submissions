class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        # Eats every pile
        right = max(piles)
        res = right

        while left <= right:
            m = (left + right) // 2

            time = 0
            for p in piles:
                time += math.ceil(float(p) / m)
            if time <= h:
                res = m
                right = m - 1
            else:
                left = m + 1
        return res

        