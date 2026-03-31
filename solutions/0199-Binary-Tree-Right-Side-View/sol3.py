# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        self.ans = []
        def solve(curr, level):
            if not curr:
                return
            
            if level == len(self.ans):
                self.ans.append(curr.val)
            
            solve(curr.right, level + 1)
            solve(curr.left, level + 1)
        
        solve(root, 0)
        return self.ans