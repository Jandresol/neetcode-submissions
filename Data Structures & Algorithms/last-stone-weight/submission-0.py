class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap - pop the largest elements
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if -x > -y:
                heapq.heappush(stones, x-y)
        if not stones:
            return 0
        return abs(stones[0])

        
        