# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        def subtree_add(node, dist):
            if not node:
                return
            if dist == k:
                res.append(node.val)
                return
            
            subtree_add(node.left, dist + 1)
            subtree_add(node.right, dist + 1)
        
        def dfs(node):
            if not node:
                return -1
            
            if node == target:
                subtree_add(node, 0)
                return 1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left != -1:
                if left == k:
                    res.append(node.val)
                else:
                    subtree_add(node.right, left + 1)
                return left + 1
            
            if right != -1:
                if right == k:
                    res.append(node.val)
                else:
                    subtree_add(node.left, right + 1)
                return right + 1
            
            return -1
        
        dfs(root)
        return res