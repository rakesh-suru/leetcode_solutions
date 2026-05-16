# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
        i = 0
        n = len(traversal)

        def dfs(depth):

            nonlocal i
            temp = i
            dash = 0

            while temp < n and traversal[temp] == '-':
                dash += 1
                temp += 1

            if dash != depth:
                return None

            i = temp

            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1

            node = TreeNode(val)

            node.left = dfs(depth + 1)
            node.right = dfs(depth + 1)

            return node

        return dfs(0)