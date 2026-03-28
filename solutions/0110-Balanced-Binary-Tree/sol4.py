class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return (True, 0)
            
            left_bal, lh = dfs(node.left)
            right_bal, rh = dfs(node.right)
            
            balanced = left_bal and right_bal and abs(lh - rh) <= 1
            
            return (balanced, 1 + max(lh, rh))
        
        return dfs(root)[0]