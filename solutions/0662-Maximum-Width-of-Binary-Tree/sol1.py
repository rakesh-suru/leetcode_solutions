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
        width = 1

        while queue:
            l = len(queue)
            first = 0
            last = 0
            for i in range(l):
                curr, val = queue.popleft()
                if i == 0:
                    first = val
                elif i == l - 1:
                    last = val
                
                if curr.left:
                    queue.append([curr.left, 2 * val + 1])
                if curr.right:
                    queue.append([curr.right, 2 * val + 2])
                
            width = max(width, last - first + 1)
        
        return width
