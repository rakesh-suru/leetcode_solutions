# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        temp = root

        while temp or stack:
            while temp:
                stack.append(temp)
                temp = temp.left
            
            temp = stack.pop()
            result.append(temp.val)

            temp = temp.right
        
        return result