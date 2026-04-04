# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 0)])
        width = 0

        while queue:
            l = len(queue)
            min_val = queue[0][1]
            first = last = 0

            for i in range(l):
                curr, val = queue.popleft()
                val -= min_val

                if i == 0:
                    first = val
                if i == l - 1:
                    last = val

                if curr.left:
                    queue.append((curr.left, 2 * val))
                if curr.right:
                    queue.append((curr.right, 2 * val + 1))

            width = max(width, last - first + 1)

        return width
