# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0

        while q:
            size = len(q)
            nodes = []

            for _ in range(size):
                node = q.popleft()
                nodes.append(node)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level % 2 == 1:
                i, j = 0, len(nodes) - 1
                while i < j:
                    nodes[i].val, nodes[j].val = nodes[j].val, nodes[i].val
                    i += 1
                    j -= 1

            level += 1

        return root