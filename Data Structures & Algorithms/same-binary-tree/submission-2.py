class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def preorder(node, nodes):
            if not node:
                nodes.append(None)
                return nodes
            
            nodes.append(node.val)
            nodes = preorder(node.left, nodes)
            nodes = preorder(node.right, nodes)

            return nodes
        
        p_preorder = preorder(p, [])
        q_preorder = preorder(q, [])

        if len(p_preorder) != len(q_preorder):
            return False

        for i in range(len(p_preorder)):
            if p_preorder[i] != q_preorder[i]:
                return False
        
        return True