class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        single_arr = []
        for arr in matrix:
            single_arr += arr
        
        l, r = 0, len(single_arr) - 1

        while l <= r:
            m = (l + r) // 2

            if (single_arr[m] < target):
                l = m + 1
                continue

            if (single_arr[m] > target):
                r = m - 1
                continue
            
            return True
        return False