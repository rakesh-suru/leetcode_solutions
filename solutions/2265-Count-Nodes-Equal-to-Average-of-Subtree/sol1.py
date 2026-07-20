# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def count_node(curr):
            if not curr:
                return 0
            return 1 + count_node(curr.left) + count_node(curr.right)
        
        def count_total(curr):
            if not curr:
                return 0
            return curr.val + count_total(curr.left) + count_total(curr.right)
        
        ans = 0
        def solve(curr):
            nonlocal ans
            if not curr:
                return
            count = count_node(curr)
            total = count_total(curr)

            if curr.val == (total // count):
                ans += 1
            
            if curr.left:
                solve(curr.left)
            if curr.right:
                solve(curr.right)
        
        solve(root)
        return ans