class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        total = len(nums)
        counted = dict.fromkeys(nums, 0.0)

        for num in counted:
            counted[num] = nums.count(num)
        
        arr = []
        for num, count in counted.items():
            arr.append([count, num])
        arr.sort()

        sorted_items = sorted(counted.items(), key=lambda item: item[1], reverse = True)
        sorted_dict = dict(sorted_items)

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res