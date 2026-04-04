# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def left_height(curr):
            if not curr:
                return 0
            height = 1
            while curr.left:
                curr = curr.left
                height += 1
            return height
        
        def right_height(curr):
            if not curr:
                return 0
            height = 1
            while curr.right:
                curr = curr.right
                height += 1
            return height

        def solve(curr):
            if not curr:
                return 0
            
            lh = left_height(curr)
            rh = right_height(curr)

            if lh == rh:
                return 2 ** lh  - 1
            
            return 1 + solve(curr.left) + solve(curr.right)
        
        ans = solve(root)
        return ans