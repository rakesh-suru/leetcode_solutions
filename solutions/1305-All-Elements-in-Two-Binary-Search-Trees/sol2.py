# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode | None, root2: TreeNode | None) -> list[int]:

        def inorder(root):
            result = []

            def traverse(node):
                if not node:
                    return

                traverse(node.left)
                result.append(node.val)
                traverse(node.right)

            traverse(root)
            return result

        a = inorder(root1)
        b = inorder(root2)

        result = []

        i = 0
        j = 0

        while i < len(a) and j < len(b):

            if a[i] <= b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1

        while i < len(a):
            result.append(a[i])
            i += 1

        while j < len(b):
            result.append(b[j])
            j += 1

        return result