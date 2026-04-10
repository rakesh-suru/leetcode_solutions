# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inorder = []

        def solve(curr):
            if not curr:
                return
            
            solve(curr.left)
            inorder.append(curr.val)
            solve(curr.right)
        
        solve(root)

        ans = float("inf")
        for i in range(1, len(inorder)):
            ans = min(ans, inorder[i] - inorder[i - 1])
        
        return ans