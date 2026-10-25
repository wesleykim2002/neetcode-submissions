class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snum = set(nums)
        longest = 0

        for num in snum:
            if (num - 1) not in snum:
                length = 1
                while (num + length) in snum:
                    length += 1
                longest = max(length, longest)
        return longest