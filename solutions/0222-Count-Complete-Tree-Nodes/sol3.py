# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def left_height(curr):
            h = 0
            while curr:
                h += 1
                curr = curr.left
            return h
        
        def right_height(curr):
            h = 0
            while curr:
                h += 1
                curr = curr.right
            return h

        def solve(curr):
            if not curr:
                return 0
            
            lh = left_height(curr)
            rh = right_height(curr)

            if lh == rh:
                return (1 << lh) - 1
            
            return 1 + solve(curr.left) + solve(curr.right)
        
        return solve(root)