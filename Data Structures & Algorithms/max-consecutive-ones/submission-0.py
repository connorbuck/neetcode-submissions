class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
                continue
            if current > result:
                result = current
            current = 0
        
        if current > result:
            result = current

        return result