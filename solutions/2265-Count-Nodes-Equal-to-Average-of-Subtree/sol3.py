# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        def dfs(node):
            if not node:
                return (0, 0, 0)

            ls, lc, la = dfs(node.left)
            rs, rc, ra = dfs(node.right)

            total = ls + rs + node.val
            cnt = lc + rc + 1

            ans = la + ra

            if node.val == total // cnt:
                ans += 1

            return (total, cnt, ans)

        return dfs(root)[2]