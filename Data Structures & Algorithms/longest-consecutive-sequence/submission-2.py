class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        nums_set = set(nums)
        nums = sorted(list(nums_set))

        longest = 1
        prevNum = nums[0]
        currentSequence = 1
        for i in range(1, len(nums)):
            currentNum = nums[i]
            if currentNum == (prevNum + 1):
                currentSequence += 1
                longest = max(longest, currentSequence)
                prevNum = currentNum
                continue
            prevNum = currentNum
            currentSequence = 1
        return max(longest, currentSequence)
