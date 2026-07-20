# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def find_depth(curr):
            if not curr:
                return 0

            left = find_depth(curr.left)
            right = find_depth(curr.right)
            return 1 + max(left, right)

        ans = 0

        def total(curr, temp):
            nonlocal ans
            if not curr:
                return

            if temp == depth:
                ans += curr.val
                return

            total(curr.left, temp + 1)
            total(curr.right, temp + 1)

        depth = find_depth(root)
        total(root, 1)
        return ans