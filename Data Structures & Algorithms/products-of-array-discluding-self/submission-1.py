class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        result = []

        prefixProduct = 1
        for i in range(len(nums)):
            prefixProduct *= nums[i]
            prefix.append(prefixProduct)
        
        postfixProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            postfixProduct *= nums[i]
            postfix.insert(0, postfixProduct)
        
        for i in range(len(nums)):
            if i == 0:
                result.append(postfix[i + 1])
                continue
            
            if i == len(nums) - 1:
                result.append(prefix[i - 1])
                continue
            
            result.append(prefix[i - 1] * postfix[i + 1])
        
        return result