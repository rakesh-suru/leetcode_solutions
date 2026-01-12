# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = []

        def dfs(node, level, level_sum):
            if not node:
                return
            
            if len(level_sum) == level:
                level_sum.append(node.val)
            else:
                level_sum[level] += node.val
            
            dfs(node.left, level + 1, level_sum)
            dfs(node.right, level + 1, level_sum)
        
        dfs(root, 0, level_sum)

        max_sum = float("-inf")
        ans = 0

        for i in range(len(level_sum)):
            if level_sum[i] > max_sum:
                max_sum = level_sum[i]
                ans = i + 1
        
        return ans