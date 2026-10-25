class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distances.append([math.sqrt((point[0])**2 + (point[1])**2), point])
        
        heapq.heapify(distances)
        
        res = []
        while k > 0:
            dist, point = heapq.heappop(distances)
            res.append(point)
            k -= 1
        return res
        
        # min_dist = distances[0]

        # res = []
        # for point in points:
        #     if min_dist == math.sqrt((point[0])**2 + (point[1])**2):
        #         res.append(point)
        # return res