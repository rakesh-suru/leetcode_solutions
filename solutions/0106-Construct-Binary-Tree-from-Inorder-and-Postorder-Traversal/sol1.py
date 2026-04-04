# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def solve(post, ino):
            if not post:
                return None
            
            curr = TreeNode(post[-1])
            
            for i, num in enumerate(ino):
                if num == post[-1]:
                    break
            
            curr.left = solve(post[: i], ino[: i])
            curr.right = solve(post[i: -1], ino[i + 1 :])
            
            return curr
        
        return solve(postorder, inorder)