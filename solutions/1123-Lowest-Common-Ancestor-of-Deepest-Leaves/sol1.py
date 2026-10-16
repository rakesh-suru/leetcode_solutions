# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:
        
        def solve(node):
            if not node:
                return (None, 0)
            
            left_lcs, left_h = solve(node.left)
            right_lcs, right_h = solve(node.right)

            if left_h == right_h:
                curr_h = 1 + left_h
                curr_lcs = node
            
            elif left_h > right_h:
                curr_h = 1 + left_h
                curr_lcs = left_lcs
            
            else:
                curr_h = 1 + right_h
                curr_lcs = right_lcs
            
            return (curr_lcs, curr_h)
        
        ans, h = solve(root)
        return ans