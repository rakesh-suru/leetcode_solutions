# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float('inf')
        level = 0
        ans = 0

        queue = deque()
        queue.append(root)

        while queue:
            level += 1
            curr_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                curr_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if curr_sum > max_sum:
                max_sum = curr_sum
                ans = level
        
        return ans