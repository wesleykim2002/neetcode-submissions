class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        types = []
        for num in nums:
            if num not in types:
                types.append(num)
            else:
                return True

        return False