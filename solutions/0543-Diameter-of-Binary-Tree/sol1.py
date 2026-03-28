# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def check(root):
            if not root:
                return 0
            return 1 + max(check(root.left) , check(root.right))
        
        ans = 0

        def find_max(root):
            nonlocal ans

            if not root:
                return 0
            
            lh = check(root.left)
            rh = check(root.right)

            ans = max(ans, lh + rh)

            find_max(root.left)
            find_max(root.right)

        find_max(root)
        return ans