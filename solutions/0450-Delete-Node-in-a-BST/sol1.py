# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        curr = root
        prev = None
        
        while curr and curr.val != key:
            prev = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        
        if not curr:
            return root
        
        def helper(node):
            if not node.left:
                return node.right
            
            if not node.right:
                return node.left
            
            temp = node.left
            while temp.right:
                temp = temp.right
            
            temp.right = node.right
            return node.left
        
        if not prev:
            return helper(curr)
        
        if prev.left == curr:
            prev.left = helper(curr)
        else:
            prev.right = helper(curr)
        
        return root