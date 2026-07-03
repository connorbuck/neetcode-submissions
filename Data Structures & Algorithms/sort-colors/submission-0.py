class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = { 0: 0, 1: 0, 2: 0}
        for num in nums:
            bucket[num] += 1
        
        counter = 0
        for key, value in bucket.items():
            for i in range(value):
                nums[counter] = key
                counter += 1