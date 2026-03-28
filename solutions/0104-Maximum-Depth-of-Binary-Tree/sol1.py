# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def solve(curr, level):
            nonlocal ans

            if not curr:
                return

            if not curr.left and not curr.right:
                ans = max(ans, level)
                return
            
            solve(curr.left, level + 1)

            solve(curr.right, level + 1)
        
        solve(root, 1)

        return ans