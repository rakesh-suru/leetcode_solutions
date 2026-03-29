# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')

        def solve(curr):
            if not curr:
                return 0
            
            leftsum = max(0, solve(curr.left))
            rightsum = max(0, solve(curr.right))

            self.maxi = max(self.maxi, curr.val + leftsum + rightsum)

            return curr.val + max(leftsum, rightsum)
        
        solve(root)
        return self.maxi