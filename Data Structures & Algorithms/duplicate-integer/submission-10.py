class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = []
        for num in nums:
            if num not in dup:
                dup.append(num)
            else:
                return True

        return False