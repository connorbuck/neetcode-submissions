class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = {}
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            self.prefix[i] = total
        

    def sumRange(self, left: int, right: int) -> int:
        leftPrefix = self.prefix[left - 1] if left > 0 else 0
        rightPrefix = self.prefix[right]

        return rightPrefix - leftPrefix
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)