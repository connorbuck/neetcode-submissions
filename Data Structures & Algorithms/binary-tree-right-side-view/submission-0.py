# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level_order = []
        d = deque([root])
        result = []

        while d:
            level = []
            d_length = len(d)

            for i in range(d_length):
                node = d.popleft()
                if node:
                    level.append(node.val)
                    d.append(node.left)
                    d.append(node.right)
            
            if level:
                level_order.append(level)

        for l in level_order:
            result.append(l[-1])
        
        return result