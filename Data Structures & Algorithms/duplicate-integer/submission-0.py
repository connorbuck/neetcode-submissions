class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = {}

        for num in nums:
            if num not in my_map:
                my_map[num] = 1
                continue
            return True
        return False