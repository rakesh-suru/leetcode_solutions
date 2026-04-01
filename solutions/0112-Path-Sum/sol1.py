# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        self.ans = False

        def solve(curr, total):
            if not curr:
                return
            
            total += curr.val

            if not curr.left and not curr.right:
                if total == targetSum:
                    self.ans = True
                return
            
            solve(curr.left, total)
            solve(curr.right, total)
        
        solve(root, 0)
        return self.ans