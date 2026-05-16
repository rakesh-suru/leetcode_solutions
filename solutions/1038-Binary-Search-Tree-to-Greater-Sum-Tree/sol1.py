# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(root)

        total = sum(ans)

        prefix = [0] * len(ans)
        prefix[0] = ans[0]

        for i in range(1, len(ans)):
            prefix[i] = prefix[i - 1] + ans[i]

        idx = 0

        def update(node):
            nonlocal idx

            if not node:
                return

            update(node.left)

            smaller_sum = prefix[idx - 1] if idx > 0 else 0
            node.val = total - smaller_sum

            idx += 1

            update(node.right)

        update(root)

        return root