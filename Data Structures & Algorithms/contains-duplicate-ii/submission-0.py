class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0

        while L < len(nums):
            my_set = set()
            R = min(len(nums), L + k + 1)

            for i in range(L, R):
                if nums[i] in my_set:
                    return True
                my_set.add(nums[i])
            
            L += 1
        
        return False