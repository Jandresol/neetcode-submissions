import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(a):
            x, y = a
            return math.sqrt((x-0)**2+(y-0)**2)
        distances = []
        for point in points:
            #  we need a max heap since we want to pop
            # the largest element
            heapq.heappush(distances, (-distance(point), point))
            if len(distances) > k:
                heapq.heappop(distances)
        return [p for (_, p) in distances]
