# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def solve_in(curr):
            nonlocal ans
            if not curr:
                return
            
            solve_in(curr.left)
            if low <= curr.val <= high:
                ans += curr.val
            solve_in(curr.right)
        
        solve_in(root)
        
        return ans