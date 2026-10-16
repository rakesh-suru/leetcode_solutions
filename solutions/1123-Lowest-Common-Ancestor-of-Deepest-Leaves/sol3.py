# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:

        def max_depth(node):
            if not node:
                return 0
            return 1 + max(
                max_depth(node.left),
                max_depth(node.right)
            )

        deepest = max_depth(root)

        def solve(node, depth):
            if not node:
                return None

            if depth == deepest:
                return node

            left = solve(node.left, depth + 1)
            right = solve(node.right, depth + 1)

            if left and right:
                return node

            return left if left else right

        return solve(root, 1)

