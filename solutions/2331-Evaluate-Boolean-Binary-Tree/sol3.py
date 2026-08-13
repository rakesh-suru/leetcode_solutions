class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def solve(node):
            if node.left is None and node.right is None:
                return node.val == 1

            if node.val == 2:
                return solve(node.left) or solve(node.right)

            return solve(node.left) and solve(node.right)

        return solve(root)