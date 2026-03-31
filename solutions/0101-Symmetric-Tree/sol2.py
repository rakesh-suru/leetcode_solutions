# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def level_order(curr, isLeft):
            if not curr:
                return []

            ans = []
            queue = deque([curr])

            while queue:
                l = len(queue)
                temp = []

                for _ in range(l):
                    node = queue.popleft()

                    if node:
                        temp.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                    else:
                        temp.append(None)

                if isLeft:
                    ans.append(temp)
                else:
                    ans.append(temp[::-1])

            return ans

        left_tree = level_order(root.left, True)
        right_tree = level_order(root.right, False)

        return left_tree == right_tree