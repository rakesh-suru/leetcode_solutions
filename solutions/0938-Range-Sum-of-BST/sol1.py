# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        inorder = []
        def solve_in(curr):
            if not curr:
                return
            
            solve_in(curr.left)
            inorder.append(curr.val)
            solve_in(curr.right)
        
        solve_in(root)
        
        ans = 0
        for num in inorder:
            if low <= num <= high:
                ans += num
        return ans