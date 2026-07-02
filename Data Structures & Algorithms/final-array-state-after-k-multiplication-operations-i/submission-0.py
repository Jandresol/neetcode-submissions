class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        import heapq
        # number and index, need number first so it can sort
        pq = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(pq)
        for _ in range(k):
            print(pq)
            x, i = heapq.heappop(pq)
            nums[i] *= multiplier
            heapq.heappush(pq, (nums[i], i))
        return nums

        