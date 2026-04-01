# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def fromNode(curr, total):
            if not curr:
                return 0
            
            total += curr.val
            count = 1 if total == targetSum else 0
            
            count += fromNode(curr.left, total)
            count += fromNode(curr.right, total)
            
            return count
        
        def solve(curr):
            if not curr:
                return 0
            
            count = fromNode(curr, 0)
            
            count += solve(curr.left)
            count += solve(curr.right)
            
            return count
        
        return solve(root)