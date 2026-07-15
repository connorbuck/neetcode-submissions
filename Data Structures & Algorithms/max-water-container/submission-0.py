class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = -1
        L, R = 0, len(heights) - 1
        
        while L < R:
            leftHeight = heights[L]
            rightHeight = heights[R]

            height = min(leftHeight, rightHeight)
            length = abs(L - R)

            area = height * length

            maxArea = max(area, maxArea)

            if leftHeight > rightHeight:
                R -= 1
                continue
            L += 1
        return maxArea