# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        temp = []

        def inorder(curr):
            if not curr:
                return
            inorder(curr.left)
            temp.append(curr.val)
            inorder(curr.right)

        inorder(root)

        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            node = TreeNode(temp[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        return build(0, len(temp) - 1)