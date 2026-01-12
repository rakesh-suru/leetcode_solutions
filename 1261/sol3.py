# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        def populate(node, val):
            node.val = val
            if node.left:
                populate(node.left, val * 2 + 1)
            if node.right:
                populate(node.right, val * 2 + 2)
        populate(root, 0)
        self.root = root

    def find(self, target: int) -> bool:
        def dfs(node):
            if not node:
                return False
            if node.val == target:
                return True
            return dfs(node.left) or dfs(node.right)
        return dfs(self.root)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)