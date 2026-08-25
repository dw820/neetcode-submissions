import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        h = []

        for point in points:
            x, y = point
            dis = x**2 + y**2
            heapq.heappush(h, (-dis, (x,y)))

            if len(h) > k:
                heapq.heappop(h)

        return [[x, y] for _, (x, y) in h]



        