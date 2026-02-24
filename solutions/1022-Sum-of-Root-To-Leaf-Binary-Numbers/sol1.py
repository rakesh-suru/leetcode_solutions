# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0

        def dfs(node, temp):
            nonlocal ans
            temp += str(node.val)
            
            if not node.left and not node.right:
                ans += int(temp, 2)
                return
            
            if node.left:
                dfs(node.left, temp)
            if node.right:
                dfs(node.right, temp)

        dfs(root, "")
        return ans