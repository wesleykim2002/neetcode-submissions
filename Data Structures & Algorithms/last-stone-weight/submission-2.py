class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while len(stones) > 1:
            x = stones.pop()
            y = stones.pop()
            if abs(x - y) > 0:
                stones.append(abs(x - y))
            stones = sorted(stones)
        
        if stones:
            return stones[0]
        else:
            return 0