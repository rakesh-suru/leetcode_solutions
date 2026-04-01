# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        
        def solve(curr, path):
            if not curr:
                return
            
            path += str(curr.val) + "->"
            
            if not curr.left and not curr.right:
                self.ans.append(path[:-2])
            else:
                solve(curr.left, path)
                solve(curr.right, path)
        
        solve(root, "")
        return self.ans