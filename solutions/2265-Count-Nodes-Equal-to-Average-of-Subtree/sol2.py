# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans

            if not node:
                return (0, 0)

            leftSum, leftCount = dfs(node.left)
            rightSum, rightCount = dfs(node.right)

            total = leftSum + rightSum + node.val
            cnt = leftCount + rightCount + 1

            if node.val == total // cnt:
                ans += 1

            return (total, cnt)

        dfs(root)

        return ans