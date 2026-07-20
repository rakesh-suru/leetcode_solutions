# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, parent, grand):
            if not node:
                return 0

            ans = 0

            if grand and grand.val % 2 == 0:
                ans += node.val

            ans += dfs(node.left, node, parent)
            ans += dfs(node.right, node, parent)

            return ans

        return dfs(root, None, None)