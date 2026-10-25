class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]

        heapq.heapify(stones)
        while len(stones) > 1:
            smashed = heapq.heappop(stones) - heapq.heappop(stones)
            if smashed:
                heapq.heappush(stones, smashed)
        if stones:
            return -stones[0] 
        else: return 0