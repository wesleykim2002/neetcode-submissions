class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = []
        for num in nums:
            if not num in visited:
                visited.append(num)
            else:
                return True
        return False