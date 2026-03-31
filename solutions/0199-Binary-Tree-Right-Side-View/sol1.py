# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([(root, 0)])
        mapper = {}
        ans = []

        while queue:
            curr, level = queue.popleft()
            mapper[level] = curr.val

            if curr.left:
                queue.append((curr.left, level + 1))
            if curr.right:
                queue.append((curr.right, level + 1))
        
        for key in sorted(mapper):
            ans.append(mapper[key])
        
        return ans
