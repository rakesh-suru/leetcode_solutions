# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.ans = []

        def solve(curr, path, total):
            if not curr:
                return
 
            total += curr.val
            path.append(curr.val)

            if not curr.left and not curr.right and total == targetSum:
                self.ans.append(path[:])
 
            solve(curr.left, path, total)
            solve(curr.right, path, total)

            path.pop()
            total -= curr.val
 
        solve(root, [], 0)
        return self.ans