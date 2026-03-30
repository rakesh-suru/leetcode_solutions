# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        cnt = 0
        queue = deque([root])

        while queue:
            size = len(queue)
            temp = []

            for _ in range(size):
                curr = queue.popleft()
                temp.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if cnt % 2 == 0:
                ans.append(temp)
            else:
                ans.append(temp[::-1])
            
            cnt += 1
        
        return ans