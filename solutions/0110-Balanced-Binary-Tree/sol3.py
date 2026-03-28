class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
             
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        def check(node):
            if not node:
                return True
            
            if abs(height(node.left) - height(node.right)) > 1:
                return False
            
            return check(node.left) and check(node.right)
        
        return check(root)