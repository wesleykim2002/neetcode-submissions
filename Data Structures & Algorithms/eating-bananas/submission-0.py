class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while (l <= r):
            m = (l + r) // 2

            time = 0
            for pile in piles:
                time += math.ceil(float(pile) / m)
            
            if time <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
            # if time > h:
            #     l = m + 1
            # elif time <= h:
            #     r = m - 1
            #     res = min(time, res)
        return res