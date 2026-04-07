# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        def solve(curr):
            if not curr:
                return None
            
            if curr.val == val:
                return curr
            
            elif curr.val < val:
                return solve(curr.right)
            
            else:
                return solve(curr.left)
        
        return solve(root)