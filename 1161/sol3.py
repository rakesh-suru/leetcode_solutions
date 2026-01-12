# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = []

        def dfs(node, level):
            if not node:
                return
            
            if level == len(level_sum):
                level_sum.append(node.val)
            else:
                level_sum[level] += node.val
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        max_sum = float('-inf')
        ans = 0
        for i, s in enumerate(level_sum):
            if s > max_sum:
                max_sum = s
                ans = i + 1
        
        return ans
