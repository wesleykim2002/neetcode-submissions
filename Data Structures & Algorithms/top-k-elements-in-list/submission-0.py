class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        total = len(nums)
        counted = dict.fromkeys(nums, 0.0)

        for num in counted:
            counted[num] = nums.count(num)/total
        
        print(counted)

        sorted_items = sorted(counted.items(), key=lambda item: item[1], reverse = True)
        sorted_dict = dict(sorted_items)

        print(sorted_dict)

        returned = []

        for key in sorted_dict:
            returned.append(key)
            if len(returned) == k:
                return returned