class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distances.append([point[0]**2 + point[1]**2, point])
        
        heapq.heapify(distances)

        res = []
        while k > 0:
            dist, point = heapq.heappop(distances)
            res.append(point)
            k -= 1
        
        return res