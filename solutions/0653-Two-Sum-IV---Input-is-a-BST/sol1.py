# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inorder = []

        def solve(curr):
            if not curr:
                return
            
            solve(curr.left)
            inorder.append(curr.val)
            solve(curr.right)
        
        solve(root)

        left = 0
        right = len(inorder) - 1

        while left < right:
            temp = inorder[left] + inorder[right]
            
            if temp == k:
                return True
            elif temp > k:
                right -= 1
            else:
                left += 1
            
        return False