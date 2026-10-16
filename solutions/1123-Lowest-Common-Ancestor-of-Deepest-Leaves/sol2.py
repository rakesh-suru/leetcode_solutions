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
                return None, 0

            left_lcs, left_h = solve(node.left)
            right_lcs, right_h = solve(node.right)

            if left_h == right_h:
                return node, 1 + left_h

            elif left_h > right_h:
                return left_lcs, 1 + left_h

            else:
                return right_lcs, 1 + right_h

        ans, _ = solve(root)
        return ans
