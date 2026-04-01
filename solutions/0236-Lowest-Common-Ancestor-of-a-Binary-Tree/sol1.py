# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.path_p = []
        self.path_q = []

        def findAnc(curr, path):
            if not curr:
                return
            
            path.append(curr)

            if curr == p:
                self.path_p = path[:]
            if curr == q:
                self.path_q = path[:]

            findAnc(curr.left, path)
            findAnc(curr.right, path)

            path.pop()

        findAnc(root, [])

        lca = None
        for u, v in zip(self.path_p, self.path_q):
            if u == v:
                lca = u
            else:
                break
        
        return lca