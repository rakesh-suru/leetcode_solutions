# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []

        def solve(curr):
            if not curr:
                return
            
            solve(curr.left)
            self.inorder.append(curr.val)
            solve(curr.right)

        solve(root)

        self.idx = -1
        self.l = len(self.inorder)


    def next(self) -> int:
        self.idx += 1
        if self.idx < self.l:
            return self.inorder[self.idx]
        return -1

    def hasNext(self) -> bool:
        if (self.idx + 1) < self.l:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()