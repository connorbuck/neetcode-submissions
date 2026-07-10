class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}

        for i in range(len(nums)):
            num = nums[i]
            if num not in my_map:
                my_map[num] = [i]
                continue
            my_map[num].append(i)
        
        for num in nums:
            complement = target - num
            if complement in my_map:
                if len(my_map[complement]) > 1:
                    return my_map[complement]
                if complement == num:
                    continue
                indices = [my_map[complement][0], my_map[num][0]]
                indices.sort()
                return indices