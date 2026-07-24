# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
            
        nodes = [root]

        while nodes:
            curr = nodes.pop()

            if not curr.left and not curr.right:
                continue
            
            temp = curr.right
            curr.right = curr.left
            curr.left = temp

            if curr.left:
                nodes.append(curr.left)
            if curr.right:
                nodes.append(curr.right)

        return root