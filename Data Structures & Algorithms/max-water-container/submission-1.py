class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            tmp = (r - l) * min(heights[r], heights[l])
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
            # if tmp > area:
            #     area = tmp
            area = max(area, tmp)
        return area