class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        result = []
        i = 0

        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    solution = [nums[i], nums[left], nums[right]]
                    result.append(solution)
                    while left < right and nums[left] == solution[1]:
                        left += 1
                    while left < right and nums[right] == solution[2]:
                        right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
            i += 1
        return result