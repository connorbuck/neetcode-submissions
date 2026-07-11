class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 0, 1

        while R < len(nums):
            if nums[L] == nums[R]:
                del nums[R]
                continue
            L += 1
            R += 1

        return len(nums)