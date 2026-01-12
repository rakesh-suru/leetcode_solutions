# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def insert(root, val):
            if not root:
                return TreeNode(val)
            if val < root.val:
                root.left = insert(root.left, val)
            else:
                root.right = insert(root.right, val)
            return root
        
        root = None
        for val in preorder:
            root = insert(root, val)
        return root