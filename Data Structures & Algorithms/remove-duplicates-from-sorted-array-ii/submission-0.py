class Solution: 
    def removeDuplicates(self, nums: List[int]) -> int:
        num_counts = {}
        R = 0

        while R < len(nums):
            if nums[R] in num_counts:
                if num_counts[nums[R]] >= 2:
                    del nums[R]
                    continue
                num_counts[nums[R]] += 1
            else:
                num_counts[nums[R]] = 1
            R += 1

        return len(nums)