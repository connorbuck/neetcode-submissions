# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # TODO: Need to perform BFS, must track with a queue
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
                result.append(level)
        
        return result