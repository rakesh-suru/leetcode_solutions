# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        row = 0
        col = 0
        queue = deque([(root, row, col)])

        while queue:
            curr, r, c = queue.popleft()
            ans.append((curr.val, r, c))

            if curr.left:
                queue.append((curr.left, r + 1, c - 1))
            if curr.right:
                queue.append((curr.right, r + 1, c + 1))

        ans.sort(key=lambda x: (x[2], x[1], x[0]))

        res = []
        prev_col = float('-inf')

        for val, r, c in ans:
            if c != prev_col:
                res.append([])
                prev_col = c
            res[-1].append(val)

        return res