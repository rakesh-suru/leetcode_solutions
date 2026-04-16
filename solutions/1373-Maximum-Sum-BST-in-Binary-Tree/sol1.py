# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def find_bst(curr, low, high):
            if not curr:
                return True
            
            if not (low < curr.val < high):
                return False
            
            return (find_bst(curr.left, low, curr.val) and
                    find_bst(curr.right, curr.val, high))

        def get_sum(curr):
            if not curr:
                return 0
            
            return curr.val + get_sum(curr.left) + get_sum(curr.right)

        def solve(curr):
            if not curr:
                return
            
            if find_bst(curr, float('-inf'), float('inf')):
                temp = get_sum(curr)
                self.ans = max(self.ans, temp)
            
            solve(curr.left)
            solve(curr.right)

        solve(root)
        return self.ans