# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def solve(preo, ino):
            if not preo:
                return None
            
            curr = TreeNode(preo[0])
            
            for i, num in enumerate(ino):
                if num == preo[0]:
                    break
            
            curr.left = solve(preo[1 : i + 1], ino[:i])
            curr.right = solve(preo[i + 1 :], ino[i + 1 :])
            
            return curr
        
        return solve(preorder, inorder)
