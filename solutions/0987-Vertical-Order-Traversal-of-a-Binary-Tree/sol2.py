# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_map = defaultdict(list)
        queue = deque([(root, 0, 0)])

        while queue:
            node, r, c = queue.popleft()
            col_map[c].append((r, node.val))

            if node.left:
                queue.append((node.left, r + 1, c - 1))
            if node.right:
                queue.append((node.right, r + 1, c + 1))

        res = []
        for col in sorted(col_map.keys()):
            temp = sorted(col_map[col])
            res.append([val for r, val in temp])

        return res