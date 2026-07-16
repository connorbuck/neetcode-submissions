class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            m = (L + R) // 2
            if nums[m] == target:
                return m
            
            # Identify which half is sorted
            if nums[L] <= nums[m]:
                # Left half is sorted
                if nums[L] <= target < nums[m]:
                    R = m - 1
                else:
                    L = m + 1
            else:
                # Right half is sorted
                if nums[m] < target <= nums[R]:
                    L = m + 1
                else:
                    R = m - 1
        return -1