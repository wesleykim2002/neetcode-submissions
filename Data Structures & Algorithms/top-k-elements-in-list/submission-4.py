class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        for num in nums:
            if num not in numCount:
                numCount[num] = 1
            else:
                numCount[num] += 1
        
        heap = []
        for num in numCount.keys():
            heapq.heappush(heap, (numCount[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res