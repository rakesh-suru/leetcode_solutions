# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        temp = cloned
        
        def dfs(node):
            if not node:
                return None

            if node.val == target.val:
                return node

            left = dfs(node.left)
            if left:
                return left

            return dfs(node.right)

        return dfs(cloned)