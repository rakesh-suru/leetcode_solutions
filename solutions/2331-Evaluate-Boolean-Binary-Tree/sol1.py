# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def solve(node):
            if not node.right or not node.left:
                return True if node.val == 1 else False
            
            if node.left and node.right:
                operation = "OR" if node.val == 2 else "AND"

                if operation == "OR":
                    return solve(node.left) or solve(node.right)
                else:
                    return solve(node.left) and solve(node.right)
        
        return solve(root)